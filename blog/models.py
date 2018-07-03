from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    post = models.TextField(max_length=1000000)
    image = models.ImageField(upload_to='images/')
