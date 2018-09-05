from django.db import models

# Create your models here.
class Stores (models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    image_link = models.CharField(max_length=2000)
    location = models.TextField(max_length=300)
    phone_number = models.CharField(max_length=10)
    facebook = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.category


    def short_description(self):
        return self.description[:100]