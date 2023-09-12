from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("thanks_list")
    else:
        form = LoginForm()

    context = {"form": form}

    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("home")


def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password != password_confirmation:
                form.add_error("the passwords do not match")
            else:
                user = User.objects.create_user(username, password=password)

                login(request, user)
                return redirect("thanks_list")
    else:
        form = SignUpForm()
        context = {
            "form": form,
        }
    return render(request, "registration/signup.html", context)
