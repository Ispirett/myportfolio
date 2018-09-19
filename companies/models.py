from django.db import models

# Create your models here.

class StoreCatagory(models.Model):
    name = models.CharField(max_length=50)

    @property
    def get_store(self):
        return Stores.objects.all()

    def __str__(self):
        return self.name


class Stores (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    image_link = models.CharField(max_length=2000)
    location = models.TextField(max_length=300)
    phone_number = models.CharField(max_length=10)
    facebook = models.CharField(max_length=1000, blank=True)
    # Todo this a unique identifier
    # this allows me to relate store catagory to each store
    store_catagory = models.ForeignKey(StoreCatagory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def short_description(self):
        return self.description[:100]



class StoreOwners (models.Model):
    name = models.CharField(max_length=50)
    # this allows me to connect many stores to one owner
    stores = models.ManyToManyField(Stores)

    def __str__(self):
        return self.name