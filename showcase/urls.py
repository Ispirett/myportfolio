from django.contrib import admin
from django.urls import include, path
from showcase import views
urlpatterns = [

    path('get_to_heaven',views.get_to_heaven, name='get_to_heaven'),
    path('snakey/',views.snakey, name='snakey')


 ]

