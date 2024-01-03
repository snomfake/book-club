from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from books.models import Book


class BookListView(ListView):
    """
    View for the homepage
    """

    queryset = Book.objects.filter(status=True)
    context_object_name = "books"
    template_name = "books/home.html"


class BookDetailView(DetailView):
    """
    View for the details page
    """

    model = Book
    context_object_name = "book"
    slug_field = "slug"
    template_name = "books/detail.html"
