from django.shortcuts import render, redirect,get_object_or_404
# require login
from django.contrib.auth.decorators import login_required
from .models import Products
from django.utils import timezone
# Create your views here.

# public variables
recent_products = Products.objects.all()[:10]



def home(request):
    products_all = Products.objects.all()
    return render(request,'products/home.html',{'recent_products': recent_products, 'products': products_all})

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
          #Redirect to detail view
          return redirect( 'trinionlinemall/products/' + str(products.id))
       else:
           return render(request, 'products/create.html', {'error', 'all fields are required'})


    else:
        return render(request, 'products/create.html')


def product_detail(request, product_id):

    product = get_object_or_404(Products, pk=product_id)
    return render(request,'products/product_details.html', {'product_detail': product, 'recent_products': recent_products})

@login_required
def upvote (request, product_id):
    if request.method == "POST":
         product = get_object_or_404(Products, pk=product_id)
         product.votes += 1
         product.save()
         return redirect('/trinionlinemall/products/' + str(product.id))

@login_required
def downvote (request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Products, pk=product_id)
        if product.votes != 1:
            product.votes -= 1
        product.save()
        return redirect('/trinionlinemall/products/' + str(product.id))