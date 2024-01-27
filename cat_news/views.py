from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

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

    return render(
        request,
        "cat_news/post_detail.html",
        {"post": post},
    )
