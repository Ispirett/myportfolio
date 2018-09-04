from django.urls import path

from django.conf.urls.static import static
from accounts import views

urlpatterns = [

    # add int url for id for blogs
    path('', views.signup, name="signup"),
    path('home/', views.home, name="home"),
]