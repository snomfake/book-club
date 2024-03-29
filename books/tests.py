from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from books.models import Author, Book, Genre


class BookTestCase(TestCase):
    """Unit test to validate http response"""

    def setUp(self):
        self.usr = get_user_model().objects.create_user(
            username="test_usr",
            password="1234"
        )
        self.author = Author.objects.create(full_name="Test author")
        self.genre = Genre.objects.create(genre="Test genre")
        self.book = Book.objects.create(
            title="Test title",
            slug="test-slug",
            body="Test body",
            image_card="/home/traxess/Projects/book-club/assets/images/d4be_1.jpg",
            image_detail="/home/traxess/Projects/book-club/assets/images/d4be_1.jpg",
            status=True,
            author=self.author,
            genre=self.genre,
        )

    def test_get_all(self):
        url = reverse("books:home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_detail(self):
        url = reverse("books:detail", args=[str(self.book.slug)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_comment_not_auth_usr(self):
        url = reverse("books:add_comment", args=[str(self.book.slug)])
        data = {
            "title": "Test title",
            "slug": "test",
            "body": "Test",
            "image_card": "/home/traxess/Projects/book-club/assets/images/d4be_1.jpg",
            "image_detail": "/home/traxess/Projects/book-club/assets/images/d4be_1.jpg",
            "status": "True",
            "author": self.author,
            "genre": self.genre
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_create_comment(self):
        self.client.login(username="test_usr", password="1234")
        url = reverse("books:add_comment", args=[str(self.book.slug)])
        data = {
            "title": "Test title",
            "slug": "test",
            "body": "Test",
            "image_card": "/home/traxess/Projects/book-club/assets/images/d4be_1.jpg",
            "image_detail": "/home/traxess/Projects/book-club/assets/images/d4be_1.jpg",
            "status": "True",
            "author": self.author,
            "genre": self.genre
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_search(self):
        url = reverse("books:search")
        data = {"q": "Test title"}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["books"],
            [repr(self.book)],
            ordered=False
        )
