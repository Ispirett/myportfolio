from django.contrib import admin
from companies.models import Stores, StoreOwners, StoreCatagory
# Register your models here.
admin.site.register(Stores)
admin.site.register(StoreOwners)
admin.site.register(StoreCatagory)