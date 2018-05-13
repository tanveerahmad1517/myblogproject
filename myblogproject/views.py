from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from posts.models import Post
from django.db.models import Q

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        qs = None
        if query:
            qs = Post.objects.filter(
                    Q(title__icontains=query)
                )
        context = {"posts": qs}
        return render(request, "search.html", context)    