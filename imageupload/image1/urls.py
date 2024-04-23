from django.urls import path
from .views import image_view, display_images

urlpatterns = [
    path('upload/', image_view),
    path('god_images/', display_images, name='god_url'),
]