from django.db import models
from django.urls import reverse


class Author(models.Model):
    """
    Model `Author` for model `Book`
    """

    full_name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.full_name)


class Genre(models.Model):
    """
    Model `Category` for model `Book`
    """

    genre = models.CharField(max_length=150)

    def __str__(self):
        return str(self.genre)


class Book(models.Model):
    """
    Book model
    """

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique_for_date="publish_date")
    body = models.TextField()
    image_card = models.ImageField(upload_to="images/", blank=True, null=True)
    image_detail = models.ImageField(upload_to="images_detail/", blank=True, null=True)
    pdf = models.FileField(upload_to="books/", blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-publish_date",)

    def __str__(self):
        return f"Book({self.title}, {self.publish_date}, {self.status})"

    def get_absolute_url(self):
        return reverse("books:detail", args=[str(self.slug)])


class Comment(models.Model):
    """
    Model `Comment` for model `Book`
    """

    username = models.CharField(max_length=150)
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-publish_date",)

    def __str__(self):
        return f"Comment({self.username}, {self.body}, {self.publish_date})"
