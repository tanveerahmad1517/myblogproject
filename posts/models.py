from __future__ import unicode_literals

import json

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from tinymce import HTMLField


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=255)
    description = HTMLField('Description')
    image = models.ImageField(upload_to="Post_images", default='media/default.png')


    def get_absolute_url(self):
        return reverse('posts:all')



    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-date',)

    def __str__(self):
        return self.title

