from django.urls import path
from . import views
from .api_views import ImageUploadAPI

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.image_list, name='image_list'),
    path('image/<int:image_id>/', views.view_image, name='view_image'),
    path('api/upload/', ImageUploadAPI.as_view(), name='image_upload_api'),
]
