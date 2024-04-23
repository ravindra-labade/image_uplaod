from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from .models import Image

def image_view(request):
    template_name = 'image1/index.html'
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Image Added Successfully')
    context = {"form": form}
    return render(request, template_name, context)




# for displaying images


def display_images(request):

	if request.method == 'GET':
		god = Image.objects.all()
		return render(request, 'image1/image.html', {'god_images': god})
