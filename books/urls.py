from django.urls import path

from books.views import BookList, BookDetail

app_name = "books"

urlpatterns = [
    path("", BookList.as_view(), name="home"),
    path("<slug:slug>/", BookDetail.as_view(), name="detail"),
]
