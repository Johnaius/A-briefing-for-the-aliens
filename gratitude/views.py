from django.shortcuts import render, redirect, get_object_or_404
from .models import Gratitude
from .forms import GratitudeForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'gratitude/home.html')

@login_required
def create_thanks(request):
    
    if request.method == "POST":
        form = GratitudeForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            print("Hurrah! form worked")
            form.save() 
         
            return redirect('thanks_list') 
    else:
        form = GratitudeForm()
        print("heres the form")
    context = {
        'form' : form,
        
    }
   
    return render(request, 'gratitude/create.html', context)


@login_required
def thanks_list(request):
    thanks = Gratitude.objects.all()
    print(thanks)
    context ={
        'thanks' : thanks,
    }
    return render(request, "gratitude/list.html", context)


@login_required
def my_list(request):
    thanks = Gratitude.objects.filter(owner=request.user)
    context ={
        'thanks' : thanks,
    }
    return render(request, "gratitude/mine.html", context)


@login_required
def show_detail(request, id):
    # get data from database
    thanks = get_object_or_404(Gratitude, id=id)
    # put data in context
    context = {
        "thanks": thanks,
    }
    # render HTML with data in contexts
    return render(request, "gratitude/detail.html", context)

def thanks_delete(request,id):
  thanks= Gratitude.objects.get(id=id)
  if request.method == "POST":
    thanks.delete()
    return redirect("thanks_list")
  
  context ={
    "thanks" : thanks
  }

  return render(request, "gratitude/delete.html", context)