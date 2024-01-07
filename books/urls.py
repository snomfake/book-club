from django.urls import path

from books.views import AddComment, BookList, BookDetail

app_name = "books"

urlpatterns = [
    path("", BookList.as_view(), name="home"),
    path("<slug:slug>/", BookDetail.as_view(), name="detail"),
    path("add/<slug:slug>/", AddComment.as_view(), name="add_comment"),
]
