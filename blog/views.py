from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):

    blogs = Blog.objects.order_by('-date')[:5] #ordered to show latest entery fist and limiting 5 on one page"""

    return render(request, 'blog_pages/all_blogs.html', {'blogs':blogs})


def detail(request, blog_id):

    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'blog_pages/detail.html', {'blog':blog})
