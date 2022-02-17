from django.contrib import admin
from .models import BlogModel


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(BlogModel, BlogAdmin)
