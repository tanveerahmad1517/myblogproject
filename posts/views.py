from django.shortcuts import render, get_object_or_404
import json
from django_ajax.decorators import ajax
# Create your views here.
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin

class AllPostList(ListView):
    model = Post
    context_object_name = 'post_list'
    paginate_by = 4
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = forms.TweetModelForm
    model = Post
    # fields = '__all__'
    template_name = 'posts/post_create.html'


class PostEditView(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'posts/post_edit.html'
class PostDeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy("posts:all")


# def posts(request):
#     all_posts = Post.objects.all()
#     paginator = Paginator(all_posts, posts_NUM_PAGES)
#     posts = paginator.page(1)
#     # likers = Post.get_likers()
#     from_Post = -1
#     if posts:
#         from_Post = posts[0].id

#     return render(request, 'posts/posts.html', {
#         'posts': posts,
#         'from_Post': from_Post,
#         'page': 1
#         # 'likers': likers
#         })


def post(request, pk):
    Post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/Post.html', {'post': post})


posts_NUM_PAGES = 10


@login_required(login_url='/login/')
def profile(request, username):
    page_user = get_object_or_404(User, username=username)
    all_posts = Post.objects.filter(user=page_user)
    paginator = Paginator(all_posts, posts_NUM_PAGES)
    posts = paginator.page(1)
    from_Post = -1
    if posts:  # pragma: no cover
        from_Post = posts[0].id

    Posts_count = Post.objects.filter(user=page_user).count()
    data = {
        'page_user': page_user,

        'bar_data': [
            Posts_count],
        'bar_labels': json.dumps('["Posts"]'),  # noqa: E501

        'posts': posts,
        'from_Post': from_Post,
        'page': 1
    }

    return render(request, 'posts/profile.html', data)
