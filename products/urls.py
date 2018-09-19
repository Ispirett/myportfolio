from django.urls import path

from django.conf.urls.static import static
from trinionlinemall import views
from blog.views import posts, all_blogs
from products import views
urlpatterns = [

    # add int url for id for blogs
   path('create/', views.create, name="create"),
   path('home', views.home, name="producthome"),
   path('<int:product_id>',views.product_detail, name="product_detail"),
   path('<int:product_id>/upvote', views.upvote, name="upvote"),
   path('<int:product_id>/downvote',views.downvote,name="downvote")
]

