from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import login_required
# Create your views here.
def all_blogs(request):
    blog = Blog.objects
    return render(request,"blog/allblogs.html",{'listblogs':blog})
# use this for getting id
def posts(request, blog_id):
    blog_post = get_object_or_404(Blog, pk=blog_id)
    return render(request,"blog/blogpost.html",{'blog_post':blog_post})
@login_required
def create_Blog(request):
    return render(request, 'blog/create.html')