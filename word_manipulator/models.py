from django.db import models

# Create your models here.
class Userfile(models.Model):
    old_word = models.CharField(max_length=255, blank=True)
    new_word = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.new_word