from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from companies.models import Stores
from blog.models import Blog
from blog.views import posts

# Create your views here.
def signup (request):
    if request.method == 'POST':
        try:
            if request.POST['password1'] == request.POST['password2']:
                # if username in database is equal to entered user name, then return error.
                User.objects.get(username=request.POST['username'])
            return render(request, "trinionlinemall/signup.html", {'error': 'Sorry username is all ready taken!'})
         # add user to database*****-
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            msg = 'SignUp Successful <br/> "<a href="home"> Go Home </a>" '
            return redirect('login')
    else:
        return render(request, "trinionlinemall/signup.html")


def login (request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)

            return redirect('home')

        else:
            return render(request, "trinionlinemall/login.html", {'error': 'Username and or Password  is incorrect!'})

    else:
        return render(request, "trinionlinemall/login.html")


def logout (request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


def home(request):

    stores = Stores.objects
    blog = Blog.objects
    blog_show = Blog.objects.get(id=1)
    return render(request, 'trinionlinemall/index.html', {'stores': stores, 'blogs': blog , 'blog_show': blog_show})










