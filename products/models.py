from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProductCatagory(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name






class Products (models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    publication_date = models.DateTimeField()
    votes = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/products//%Y/%m/')
    icon = models.ImageField(upload_to='images/products/icons/%Y/%m/%d/')
    url = models.TextField(max_length=1000)
    body = models.TextField(max_length=1000)
    user_hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    product_catagory = models.ForeignKey(ProductCatagory, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    def summary (self):
        return self.body[:100]

    def pub_date (self):
        return self.publication_date.strftime('%b %e %Y')