from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def add_category(request):
    pass

def add_tag(request):
    if request.method == "POST":
        name = request.POST.get('tag')
        if len(name) > 2:
            t = Tag(name=name) # new object of Tag
            t.save() # save to database
        return render(request,'partials/tag_form.html')   
    return HttpResponse("<p>Invalid request</p>")

def upload_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('images')
    ctx = {'form': ImageForm()}
    return render(request,
            'upload_image.html', 
            ctx)

def delete_image(request, id):
    try:
        image = Image.objects.get(id=id)
        image.delete()
    except:
        pass
    return render(request, 'partials/image_list.html', {'images': Image.objects.all()})

def view_categories(request):
    categories = Category.objects.all()
    return render(request, "index.html", {'categories': categories})

def view_tags(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags': tags})

def view_images(request):
    images = Image.objects.all()
    return render(
        request,
        'index.html',
        {'images': images}
    )


def get_tags(request):
    tags = Tag.objects.all()
    return render(request, 'partials/tag_list.html', {'tags': tags})