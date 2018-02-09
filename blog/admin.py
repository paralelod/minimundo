from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
# admin pwd: hellomundo
admin.site.register(Comment)