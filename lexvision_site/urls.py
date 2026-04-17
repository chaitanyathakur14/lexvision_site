from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from processor import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Use views.function_name for both paths
    path('', views.upload_judgment, name='upload'), 
    path('ask-document/', views.ask_document, name='ask_document'),
]

# This allows the browser to see the uploaded images/PDFs during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)