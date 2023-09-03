from django.shortcuts import render, redirect
from .models import Gratitude, Photo
from .forms import GratitudeForm, PhotoForm
from django.http import HttpResponse
from cloudinary.forms import cl_init_js_callbacks 

# Create your views here.
def create_thanks(request):
    photo_form = dict( backend_form = PhotoForm())
    if request.method == "POST":
        form = GratitudeForm(request.POST)
        photo = PhotoForm(request.POST, request.FILES)
        photo_form['posted'] = form.instance
        if form.is_valid() and photo.is_valid():
            form.save()
            photo.save()  
        return redirect('home') 
    else:
        form = GratitudeForm()
        photo = PhotoForm()
    context = {
        'form' : form,
        'photo' : photo
    }

    return render(request, 'gratitude/create.html', context)

def receipt_list(request):
     # This line creates a queryset that filters Receipt objects
    # to only include those where the purchaser is the logged-in user.
    photos = Photo.objects.all()
    thanks = Gratitude.objects.all()
    context ={
        'thanks' : thanks,
        'photo' : photos,
    }
    return render(request, "gratitude/list.html", context)
