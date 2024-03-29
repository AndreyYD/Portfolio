from django.shortcuts import render, get_object_or_404
from .models import BlogModel


def all_blogs(request):
    blogs = BlogModel.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blog.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(BlogModel, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
