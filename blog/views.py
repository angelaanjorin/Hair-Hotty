from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from profiles.models import UserProfile

# Create or edit a post.


class PostCreateOrUpdateView(
        LoginRequiredMixin, UserPassesTestMixin, CreateView, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Check if this is an update or a new creation
        if self.get_object():
            form.instance.author = self.request.user
            response = super().form_valid(form)
            messages.success(self.request, "Post updated successfully!")

            user_profile = UserProfile.objects.get(user=form.instance.author)
            return redirect(reverse('my_posts', kwargs={'profile_id': user_profile.id}))


        else:  # If no object exists, it´s a new post creation
            form.instance.author = self.request.user
            response = super().form_valid(form)

            if self.object.status == 0:
                messages.info(
                    self.request,
                    'Your Post has been submitted and is awaiting approval.')

        return response

    def test_func(self):
        return UserProfile.objects.filter(user=self.request.user).exists()


    def get_object(self, get_queryset=None):
        post_id = self.kwargs.get('pk')
        if post_id:
            return Post.objects.get(pk=post_id)
        return None


# Post delete view for all registered users
def post_delete_view(request, pk):
    """ View to delete a post
    """
    # Fetch the post using the primary key(pk)
    post = get_object_or_404(Post, pk=pk, author=request.user)

    # check if the current user is the author of the Post
    if post.author == request.user:
        post.delete()
        messages.success(request, "Post deleted successfully!")
    else:
        messages.error(request, "You can only delete your own post")

    return redirect(reverse('my_posts', kwargs={'profile_id': user_profile.id}))


class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts.
    **Context**"""
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        context = super(PostList, self).get_context_data(*args, **kwargs)
        
        return context


class post_detail(View):
    """
    Display an individual :model:`blog.Post`.

    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("-created_on")
        comment_count = post.comments.all().count()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            },)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been posted and you can edit or delete it!'
            )
            # Resets the form after comment submission
            comment_form = CommentForm()
        else:
            messages.add_message(
                request, messages.ERROR, "Error posting your comment."
            )

        # Re-fetch the comments and comment count after the
        # new comment is posted
        comments = post.comments.all().order_by("-created_on")
        comment_count = comments.count()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_count": comment_count,
                "comment_form": comment_form,
                "liked": liked
            },
        )


def comment_edit(request, slug, comment_id):
    """View to edit comments"""
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Comment updated successfully!')
        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request,
                             messages.SUCCESS,
                             'Your comment has been deleted!')
    else:
        messages.add_message(request,
                             messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostLike(View):
    """
    Toggles like status on submission of like button on posts.
    Also sends success message to author
    Login required
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Thanks for liking the post!')

        return HttpResponseRedirect(reverse(
            'post_detail', args=[slug]))






