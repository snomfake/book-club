from django.urls import path

from registration.views import Login

app_name = "registration"

urlpatterns = [
    path("login/", Login.as_view(), name="login")
]
