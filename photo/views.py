from email.mime import image
from multiprocessing import context
from unicodedata import category
from django.shortcuts import redirect, render
from .models import Category,Photo


#project by rajat 
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:    
        photos = Photo.objects.filter(category__name =category )

    categories = Category.objects.all()
    context = {
        'categories':categories,
        'photos' :photos
    }
    return render(request,'photo/gallery.html',context)

def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    context ={
        'photo' :photo
    }
    return render(request,'photo/photo.html',context)

def addPhoto(request):
    categories = Category.objects.all()
    if request.method == 'POST' :
        data = request.POST 
        image = request.FILES.get('image')
        if data['category']!='none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new']!='':
            category , created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            title = data['title'],
            image = image

        )
        return redirect('gallery')

    context = {
        'categories':categories
    }
    return render(request,'photo/add.html',context)

# 51:00 to start 
def delete_photo(request,pk=None):   
    Photo.objects.get(id=pk).delete()
    return redirect('gallery')