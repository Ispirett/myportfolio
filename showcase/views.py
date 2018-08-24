from django.shortcuts import render

# Create your views here.
def get_to_heaven(request):
    return render(request, 'showcase/get_to_heaven.html')


def snakey(request):
    return render(request, 'showcase/snakey.html')