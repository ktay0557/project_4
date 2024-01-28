from django import forms
from .models import Comment, Post


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


class PostForm(forms.ModelForm):
    """
    Form class for the users to post their content.
    """
    class Meta:
        """
        Specifies the Django model and the order of the fields.
        """
        model = Post
        fields = ('title', 'content', 'excerpt', 'featured_image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set the required to false, so user can choose to include image
        self.fields['featured_image'].required = False
        # set excerpt required to true, so the user must include one
        self.fields['excerpt'].required = True
