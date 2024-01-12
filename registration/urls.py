from django.urls import path

from registration.views import signin_view, signup_view, logout_view

app_name = "registration"

urlpatterns = [
    path("signin/", signin_view, name="signin"),
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
]

