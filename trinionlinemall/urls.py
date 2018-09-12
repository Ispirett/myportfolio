from django.urls import path

from django.conf.urls.static import static
from trinionlinemall import views
from blog.views import posts, all_blogs

urlpatterns = [

    # add int url for id for blogs
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('home/', views.home, name="home"),
    path('<int:blog_id>/',posts, name='posts'),
    path('allblogs/', all_blogs, name="all_blogs")
]

