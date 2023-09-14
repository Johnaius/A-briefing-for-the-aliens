from django.shortcuts import render, redirect, get_object_or_404
from comments.forms import CommentsForm
from comments.models import Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_comment(request):
    
    if request.method == "POST":
        # We should use the form to validate the values
        #   and save them to the database
        form = CommentsForm(request.POST)
        
        if form.is_valid():
            form.instance.user = request.user
            
            form.save()
            # If all goes well, we can redirect the browser
            #   to another page and leave the function
            
            print("success")
            return redirect("thanks_list")
    else:
        # Create an instance of the Django model form class
        print("Fail")
        form = CommentsForm()

    # Put the form in the context
    context = {
        "form": form,
    }
    # Render the HTML template with the form
    return render(request, "comments/create.html", context)



