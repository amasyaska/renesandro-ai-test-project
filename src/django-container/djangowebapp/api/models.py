from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])

class CustomUser(User):
    pass


class Task(models.Model):

    name = models.CharField()
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to=content_file_name)
    prompt = models.CharField()