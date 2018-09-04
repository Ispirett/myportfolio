from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse

# Create your views here.
def signup (request):
    if request.method == 'POST':
        try:
            if request.POST['password1'] == request.POST['password2']:
                # if username in database is equal to entered user name, then return error.
                User.objects.get(username=request.POST['username'])
            return render(request, "accounts/signup.html", {'error': 'Sorry username is all ready taken!'})
         # add user to database
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            msg = 'SignUp Successful <br/> "<a href="home"> Go Home </a>" '
            return HttpResponse(msg )
    else:
        return render(request, "accounts/signup.html")











def login (request):
    return render(request, "accounts/login.html")


def logout (request):
    return render(request, "accounts/logout.html")


def home (request):
    return render(request, 'accounts/index.html')