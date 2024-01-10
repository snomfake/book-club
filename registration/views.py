from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views.generic import View


class Login(View):
    """Login"""

    def get(self, request):
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "registration/login.html", context)

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
        return render(request, "registration/login.html", context)
