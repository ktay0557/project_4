from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm

# Create your views here.


class NewsList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "cat_news/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`cat_news.Post`.

    **Context**

    ``post``
        An instance of :model:`cat_news.Post`.

    **Template:**

    :template:`cat_news/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    return render(
        request,
        "cat_news/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )
