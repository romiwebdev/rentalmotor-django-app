from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rental.urls', namespace='rental')),  # Mengarahkan ke URL aplikasi rental
]

# Konfigurasi untuk file media (gambar motor)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
