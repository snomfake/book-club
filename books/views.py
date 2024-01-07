from django.views.generic import View
from django.shortcuts import redirect, render, get_object_or_404
from books.forms import CommentForm

from books.models import Book


class BookList(View):
    """List all book"""

    def get(self, request):
        books = Book.objects.filter(status=True)
        context = {"books": books}
        return render(request, "books/home.html", context)


class BookDetail(View):
    """Retrieve a book instance"""

    def get(self, request, slug: str):
        book = get_object_or_404(Book, slug=slug)
        context = {"book": book}
        return render(request, "books/detail.html", context)


class AddComment(View):
    """sss"""

    def post(self, request, slug: str):
        book = get_object_or_404(Book, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.book = book
            form.save()

        return redirect("/")
