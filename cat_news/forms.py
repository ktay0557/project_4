from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form class for the users to comment on posts.
    """
    class Meta:
        """
        Specifies the Django model and the order of the fields.
        """
        model = Comment
        fields = ('body',)
