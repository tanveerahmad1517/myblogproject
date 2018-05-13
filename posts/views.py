from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic import ListView, DetailView

class AllPosts(ListView):
    model = Post
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
