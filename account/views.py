from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'posts/profile.html', args)