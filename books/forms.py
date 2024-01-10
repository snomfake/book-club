from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from books.models import Book, Comment


class CommentForm(forms.ModelForm):
    """Comment form"""

    class Meta:
        model = Comment
        fields = ("username", "body")


class BooktAdminForm(forms.ModelForm):
    """CKEditor form for the `body` field of the `Book` model"""

    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Book
        fields = "__all__"
