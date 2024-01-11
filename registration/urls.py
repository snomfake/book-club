from django.urls import path, reverse_lazy

from registration.views import SignIn, SignUp, Logout

app_name = "registration"

urlpatterns = [
    path("signin/", SignIn.as_view(), name="signin"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("logout/", Logout.as_view(), name="logout"),
]

