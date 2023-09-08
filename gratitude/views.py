from django.shortcuts import render, redirect
from .models import Gratitude
from .forms import GratitudeForm
from django.http import HttpResponse
from cloudinary.forms import cl_init_js_callbacks 

# Create your views here.
def create_thanks(request):
    
    if request.method == "POST":
        form = GratitudeForm(request.POST, request.FILES)
        print(form.cleaned_data())
        if form.is_valid():
            print("Hurrah! form worked")
            form.save() 
         
            return redirect('thanks_list') 
    else:
        form = GratitudeForm()
        print("fail!")
    context = {
        'form' : form,
        
    }
   
    return render(request, 'gratitude/create.html', context)

def thanks_list(request):
    thanks = Gratitude.objects.all()
    context ={
        'thanks' : thanks,
    }
    return render(request, "gratitude/list.html", context)
