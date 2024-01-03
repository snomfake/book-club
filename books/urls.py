from django.urls import path

from books.views import BookListView, BookDetailView

app_name = "books"

urlpatterns = [
    path("<slug:slug>/", BookDetailView.as_view(), name="detail"),
    path("", BookListView.as_view(), name="home"),
]
