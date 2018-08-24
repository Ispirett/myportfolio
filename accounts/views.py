from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup (request):
    if request.method == 'POST':
        try:
            if request.POST['password1'] == request.POST['password2']:

                User.objects.get(username=request.POST['username'])
            return render(request, "accounts/signup.html", {'error': 'Sorry username is all ready taken!'})

        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            redirect('signup')
    else:
        return render(request, "accounts/signup.html")











def login (request):
    return render(request, "accounts/login.html")


def logout (request):
    return render(request, "accounts/logout.html")
