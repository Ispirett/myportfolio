from django.urls import path

from django.conf.urls.static import static
from trinionlinemall import views
from blog.views import posts, all_blogs
from products import views
urlpatterns = [

    # add int url for id for blogs
   path('create/', views.create, name="create"),
   path('home', views.home, name="producthome")
]

