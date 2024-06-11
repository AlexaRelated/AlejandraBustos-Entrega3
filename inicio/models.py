from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render
from django.utils.text import slugify
from django.utils import timezone


class Author(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='inicio_author')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

def index(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'inicio/index.html', {'posts': posts})

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=100)  # Campo de categoría

    def __str__(self):
        return self.title