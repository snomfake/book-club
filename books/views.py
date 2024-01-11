from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View

from books.forms import CommentForm
from books.models import Book

from django.contrib.auth.views import PasswordChangeView

class BookList(View):
    """List all book"""

    def get(self, request):
        obj_list = Book.objects.filter(status=True)

        paginator = Paginator(obj_list, 6)
        page = request.GET.get("page")

        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)

        context = {"books": books}
        return render(request, "books/home.html", context)


class BookDetail(View):
    """Retrieve a book instance"""

    def get(self, request, slug: str):
        book = get_object_or_404(Book, slug=slug)
        comments = book.comment_set.filter(active=True)
        context = {"book": book, "comments": comments}
        return render(request, "books/detail.html", context)


class AddComment(View):
    """Add comment"""

    def post(self, request, slug: str):
        book = get_object_or_404(Book, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.book = book
            form.save()

        return redirect(book.get_absolute_url())


class Search(View):
    """Search"""

    def get(self, request):
        q = request.GET.get("q")

        books = Book.objects.annotate(
            search=SearchVector("title", "author__full_name")
        ).filter(search=q)

        context = {"books": books, "q": q}
        return render(request, "books/home.html", context)
