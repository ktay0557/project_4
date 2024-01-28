from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm

# Create your views here.


class NewsList(generic.ListView):
    """
    Returns all the published posts in :model:`cat_news.Post`,
    and displays them in a page of nine posts.

    **Context**

    ``queryset``
        All published instances of :model:`cat_news.Post`
    ``paginated_by``
        The number of posts to a page.

    **Template:**

    :template:`cat_news/index.html`
    """
    queryset = Post.objects.filter(status=1)
    template_name = "cat_news/index.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        """
        Pass an instance of the form to the template
        """
        context = super().get_context_data(**kwargs)
        context['post_form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
         """
         Display an instance of :form:`cat_news.postForm`.

         **Context**

         ``post_form``
         An instance of :form:`cat_news.postForm`.
         Allows user to post a story.

         **Template:**
         :template:`cat_news/index.html`
         """
        if request.method == "POST":
            post_form = PostForm(data=request.POST)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.author = request.user
                post.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Your story has been submitted and is awaiting approval'
                )
                return redirect('home')


def post_detail(request, slug):
    """
    Display an individual :model:`cat_news.Post`.

    **Context**

    ``post``
        An instance of :model:`cat_news.Post`.
    ``comments``
        All o9f the approved comments relating to the post.
    ``comment_count``
        A count of all the approved comments relating to the post.
    ``comment_form``
        An instance of :form:`cat_news.CommentForm`

    **Template:**

    :template:`cat_news/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been submitted and is awaiting approval'
            )

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


def comment_edit(request, slug, comment_id):
    """
    Displays a single comment for editting.

    **Context**

    ``post``
        An instance of :model:`cat_news.Post`.
    ``comment``
        A single comment relating to the post.
    ``comment_form``
        An instance of :form:`cat_news.CommentForm`.
    """
    if request.method == 'POST':

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 'Your comment has been updated'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'There was an error updating your comment'
            )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    To delete a single comment.

    **Context**

    ``post``
        An instance of :model:`cat_news.Post`.
    ``comment``
        A single comment relating to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Your comment has been deleted'
        )
    else:
        messages.add_message(
            request, messages.ERROR, 'There was an error deleting this comment'
        )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
