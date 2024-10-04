from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageUploadForm
from django.http import FileResponse
from .models import UploadedImage

def upload_image(request):
    """Вьюшка для загрузки через веб-форму"""
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'images/upload_image.html', {'form': form})


def image_list(request):
    """Вьюшка для просмотра списка изображений и их ссылок"""
    images = UploadedImage.objects.all()
    return render(request, 'images/image_list.html', {'images': images})


def view_image(request, image_id):
    """Вьюшка для отображения изображения по статической ссылке"""
    image = get_object_or_404(UploadedImage, pk=image_id)
    return FileResponse(image.image)