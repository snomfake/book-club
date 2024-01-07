from django import forms

from books.models import Comment


class CommentForm(forms.ModelForm):
    """
    sss
    """

    class Meta:
        model = Comment
        fields = ("username", "body")
