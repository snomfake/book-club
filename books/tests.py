from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch

from books.models import Author, Book, Genre


class BookTestCase(TestCase):
    """
    Unit test to validate http response
    """

    def setUp(self):
        self.author = Author.objects.create(full_name="Test author")
        self.genre = Genre.objects.create(genre="Test genre")
        self.book = Book.objects.create(
            title="Test title",
            slug="test-slug",
            body="Test body",
            status=True,
            author=self.author,
            genre=self.genre,
        )

    def test_get_all(self):
        url = reverse("books:home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @patch("books.models.Book.image", None)
    def test_get_detail(self):
        url = reverse("books:detail", args=[str(self.book.slug)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
