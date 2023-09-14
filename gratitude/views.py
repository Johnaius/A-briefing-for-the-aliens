from django.shortcuts import render, redirect, get_object_or_404
from .models import Gratitude
from .forms import GratitudeForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
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

@login_required
def create_thanks(request):
    # Check if the request method is POST (i.e., form submission).
    if request.method == "POST":
        # Create an instance of the GratitudeForm with POST data and files.
        form = GratitudeForm(request.POST, request.FILES)
        # Check if the form is valid.
        if form.is_valid():
            # Set the owner of the form instance to the current user.
            form.instance.owner = request.user
            # Print a message to indicate the form submission was successful.
            print("Hurrah! form worked")
            # Save the form data to the database.
            form.save()
            # Redirect the user to the 'thanks_list' view after successfully adding gratitude.
            return redirect('thanks_list')
    else:
        # If the request method is not POST, create an empty GratitudeForm instance.
        form = GratitudeForm()
        # Print a message to indicate that the form is being displayed.
        print("heres the form")
    
    # Create a context dictionary containing the 'form'.
    context = {
        'form' : form,
    }
    
    # Render the 'create.html' template with the context data.
    return render(request, 'gratitude/create.html', context)

# Define a 'home' view that renders the 'home.html' template.
def home(request):
    return render(request, 'gratitude/home.html')

# Decorator ensures that only logged-in users can access this view.
@login_required
def thanks_list(request):
    # Retrieve all Gratitude objects from the database.
    thanks = Gratitude.objects.all()
    # Print the 'thanks' queryset.
    print(thanks)
    # Create a context dictionary containing the 'thanks'.
    context ={
        'thanks' : thanks,
    }
    # Render the 'list.html' template with the context data.
    return render(request, "gratitude/list.html", context)

# Decorator ensures that only logged-in users can access this view.
@login_required
def my_list(request):
    # Retrieve Gratitude objects associated with the current user.
    thanks = Gratitude.objects.filter(owner=request.user)
    # Create a context dictionary containing the 'thanks'.
    context ={
        'thanks' : thanks,
    }
    # Render the 'mine.html' template with the context data.
    return render(request, "gratitude/mine.html", context)

# Define a 'thanks_delete' view that allows deleting a gratitude entry.
def thanks_delete(request, id):
    # Retrieve the Gratitude object with the specified ID.
    thanks = Gratitude.objects.get(id=id)
    # Check if the request method is POST (i.e., deletion confirmation).
    if request.method == "POST":
        # Delete the gratitude entry.
        thanks.delete()
        # Redirect the user to the 'thanks_list' view after deletion.
        return redirect("thanks_list")
    
    # Create a context dictionary containing the 'thanks'.
    context = {
        "thanks" : thanks
    }

    # Render the 'delete.html' template with the context data.
    return render(request, "gratitude/delete.html", context)