from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
