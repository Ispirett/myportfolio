from django.shortcuts import render, redirect
# require login
from django.contrib.auth.decorators import login_required
from .models import Products
from django.utils import timezone
# Create your views here.

def home(request):
    return render(request,'products/home.html')

@login_required
def create (request):
    if request.method == 'POST':
       if request.POST['title'] and request.POST['link'] and request.POST['description'] and request.FILES['icon'] and request.FILES['image']:
          products = Products()
          products.title = request.POST['title']
          # adds http or https if there is not  any
          if request.POST['link'].startswith('http://') or request.POST['link'].startswith('https://'):
             products.url = request.POST['link']
          else:
              products.url = 'https://' + request.POST['link']
          products.body = request.POST['description']
          products.icon = request.FILES['icon']
          products.image = request.FILES['image']
          products.publication_date = timezone.datetime.now()
          products.user_hunter = request.user
          products.save()
          return redirect('home')
       else:
           return render(request, 'products/create.html', {'error', 'all fields are required'})


    else:
        return render(request, 'products/create.html')



