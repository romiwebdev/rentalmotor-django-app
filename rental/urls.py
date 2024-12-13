# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'rental'

urlpatterns = [
    path('', views.home, name='home'),
    path('motor/<int:motor_id>/', views.motor_detail, name='motor_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Menambahkan ini untuk file media
