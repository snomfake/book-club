from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View


class SignIn(View):
    """Login in system"""

    def get(self, request):
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "registration/signin.html", context)

    def post(self, request):
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


class SignUp(View):
    """Registration a new user"""

    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("registration:signin")

        context = {"form": form}
        return render(request, "registration/signup.html", context)


class Logout(View):
    """Logout is system"""

    def get(self, request):
        logout(request)
        return redirect("books:home")

