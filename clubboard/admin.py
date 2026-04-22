from django.contrib import admin
from .models import reply, Post, Club

# Register your models here.
admin.site.register(Club)
admin.site.register(Post)
admin.site.register(reply)