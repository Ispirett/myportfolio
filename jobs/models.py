from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=40)
    summary = models.CharField(max_length=200)
