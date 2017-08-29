from django.contrib import admin
from forum.models import Post, Thread

# Register your models here.
admin.site.register(Thread)
admin.site.register(Post)