import site
from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Project, ProjectAdmin)
