from django.shortcuts import render
from .models import Blog

# Create your views here.
def all_blogs(request):
    blog = Blog.objects
    return render(request,"blog/allblogs.html",{'listblogs':blog})

