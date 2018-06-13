from django.shortcuts import render, get_object_or_404
import json
from django_ajax.decorators import ajax
# Create your views here.
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from . import forms

class AllPostList(ListView):
    model = Post
    context_object_name = 'post_list'
    paginate_by = 4
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
class PostCreateView(CreateView):
    form_class = forms.PostForm
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




