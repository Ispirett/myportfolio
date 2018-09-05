from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    link = models.CharField(max_length=1000)
    title = models.CharField(max_length=40)
    summary = models.CharField(max_length=200)


    def __str__(self):
        return self.title