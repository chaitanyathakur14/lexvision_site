import os
import pytesseract
from pdf2image import convert_from_path

# --- YOUR PATHS ---
POPPLER_PATH = r'C:\Users\CHAITANYA THAKUR\Downloads\Release-25.12.0-0\poppler-25.12.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def check_systems():
    print("🔍 Starting LexVision Diagnostics...")
    
    # 1. Check Tesseract
    if os.path.exists(pytesseract.pytesseract.tesseract_cmd):
        print("✅ Tesseract Engine: FOUND")
        try:
            version = pytesseract.get_tesseract_version()
            print(f"   Version: {version}")
        except:
            print("   ⚠️ Tesseract exists but Python can't run it.")
    else:
        print("❌ Tesseract Engine: NOT FOUND at the specified path.")

    # 2. Check Poppler
    if os.path.exists(POPPLER_PATH):
        print("✅ Poppler Path: VALID")
        # Check if pdfinfo.exe is inside
        if os.path.exists(os.path.join(POPPLER_PATH, "pdfinfo.exe")):
            print("   ✅ Poppler Binaries: VERIFIED")
        else:
            print("   ⚠️ Poppler folder found, but 'pdfinfo.exe' is missing inside 'bin'.")
    else:
        print("❌ Poppler Path: INVALID")

if __name__ == "__main__":
    check_systems()