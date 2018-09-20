from django.contrib import admin
from.models import Products, ProductCatagory
# Register your models here.

admin.site.site_header = 'Ispirett Adminisitration'
admin.site.site_title = 'Ispire Enterprise'
admin.site.index_title = 'Ispire Enterprise'

admin.site.register(Products)
admin.site.register(ProductCatagory)