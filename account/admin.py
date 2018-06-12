from django.contrib import admin

# Register your models here.
from .models import Profile
class DeleteFileType(object):
    def __nonzero__(self):
        return False

DeleteFile = DeleteFileType()
admin.site.register(Profile)
