import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from google import genai
from .utils import run_lexvision_pipeline


@csrf_exempt
def ask_document(request):
    if request.method == "POST":
        user_query = request.POST.get('question', '').strip()
        doc_text = request.POST.get('context', '').strip()

        api_key = getattr(settings, 'GEMINI_API_KEY', None) or os.getenv('GEMINI_API_KEY')

        if not api_key:
            return JsonResponse({'answer': "AI Error: GEMINI_API_KEY is missing."}, status=500)

        try:
            client = genai.Client(api_key=api_key)
            prompt = f"""
            You are 'LexVision AI', a legal research assistant.
            Answer the question based on the judgment text.

            TEXT: {doc_text[:15000]}
            QUESTION: {user_query}
            """
            response = client.models.generate_content(model="gemini-3-flash-preview", contents=prompt)
            return JsonResponse({'answer': response.text})
        except Exception as e:
            return JsonResponse({'answer': f"AI Error: {str(e)}"}, status=500)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


def upload_judgment(request):
    if request.method == 'POST' and request.FILES.get('document'):
        myfile = request.FILES['document']

        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_path = fs.path(filename)

        output_dir = settings.MEDIA_ROOT
        os.makedirs(output_dir, exist_ok=True)

        results = run_lexvision_pipeline(uploaded_file_path, output_dir)

        print("DEBUG: Pipeline returned keys ->", list(results.keys()))

        # CRITICAL FIX: Normalize step keys to match template exactly
        steps = results.get('steps', {})
        normalized_steps = {}
        for key, value in steps.items():
            if value and isinstance(value, str):
                # Keep only the filename, not full path
                normalized_steps[key] = os.path.basename(value)

        context = {
            'original_url': fs.url(filename),
            'extracted_text': results.get('text', ''),
            'verified': results.get('is_verified', False),
            'case_name': results.get('case_no', "Unknown Case"),
            'category': results.get('category', 'Unknown'),
            'confidence': results.get('confidence', '0%'),
            'ipc_section': results.get('ipc_section', 'N/A'),
            'year': results.get('year', 'N/A'),
            'model_confidence': results.get('model_confidence', '98.0%'),
            'steps': normalized_steps,        # ← Use normalized steps
            'error': results.get('error')
        }

        return render(request, 'processor/results.html', context)

    return render(request, 'processor/upload.html')