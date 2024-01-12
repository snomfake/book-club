from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Login in system
def signin_view(request):
    form = AuthenticationForm(request, request.POST)

    if form.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")

        usr = authenticate(request, username=username, password=password)

        if usr is not None:
            login(request, usr)
            return redirect("books:home")

    context = {"form": form}
    return render(request, "registration/signin.html", context)


# Registration a new user
def signup_view(request):
    form = UserCreationForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect("registration:signin")

    context = {"form": form}
    return render(request, "registration/signup.html", context)


# Logout is system
@login_required()
def logout_view(request):
    logout(request)
    return redirect("books:home")

