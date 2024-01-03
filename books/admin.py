from django.contrib import admin

from books import models


class CommentInline(admin.StackedInline):
    """
    Inline class for managing comments related to a book in the admin panel
    """

    model = models.Comment
    extra = 1


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Add model `Author` to admin panel
    """

    pass


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Add model `Genre` to admin panel
    """

    pass


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    """
    Add model `Book` to admin panel
    """

    list_display = ("title", "author", "publish_date", "status")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "publish_date"
    ordering = ("status", "publish_date")
    inlines = [CommentInline]
    save_on_top = True


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add model `Comment` to admin panel
    """

    list_filter = ("username", "publish_date", "active")
    readonly_fields = ("username", "body")

