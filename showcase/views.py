from django.shortcuts import render


# Create your views here.
def get_to_heaven(request):
    return render(request, 'showcase/get_to_heaven.html',)

def update_log (request):
    return render(request, 'showcase/updatelog.html')


def snakey(request):
    return render(request, 'showcase/snakey.html')



def ispire_shooter(request):
    return render(request, 'showcase/index.html')