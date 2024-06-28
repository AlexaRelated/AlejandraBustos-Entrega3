
from django.contrib import admin
from .models import Post
from .forms import PostForm
from .models import Profile

class PostAdmin(admin.ModelAdmin):
    form = PostForm

admin.site.register(Post, PostAdmin)
admin.site.register(Profile)