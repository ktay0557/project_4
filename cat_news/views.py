from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class NewsList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "cat_news/index.html"
    paginate_by = 6
