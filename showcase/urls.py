from django.contrib import admin
from django.urls import include, path
from showcase import views
urlpatterns = [

    path('get_to_heaven',views.get_to_heaven, name='get_to_heaven'),
    path('snakey/',views.snakey, name='snakey'),
    path('ispireshooter/', views.ispire_shooter, name='ispire_shooter'),
    path('get_to_heaven/updatelog/', views.update_log, name="updatelog")
 ]

