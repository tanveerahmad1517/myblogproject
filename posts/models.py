from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    users = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=120)
    title_html = models.TextField(editable=False)
    content = models.TextField()
    image = models.ImageField(upload_to="Post_images", default='media/default.png')
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False,auto_now_add=False,)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title