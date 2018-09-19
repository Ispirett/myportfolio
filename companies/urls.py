
from django.contrib import admin
from django.urls import path, include
from companies import views
from rest_framework import routers

from rest_framework.urlpatterns import format_suffix_patterns

#urlpatterns = [
 #            path( 'stores/',views.StoreList.as_view())

#]

#urlpatterns = format_suffix_patterns(urlpatterns)
# todo work on rest api
# routers maps all my fields in the database to urls
router = routers.DefaultRouter()
router.register('stores',views.StoreView)
router.register('storescatagory',views.StoreCatatgoryView)
router.register('storeowners',views.StoreOwnersView)
urlpatterns = [
     path('', include(router.urls)),
     path('home/',views.company_home,name="company_home"),
     path('<int:company_id>', views.company_details, name="company_details"),
     path('list/', views.company_list, name="company_list"),
]