from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    post = models.TextField(max_length=1000000)
    image = models.ImageField(upload_to='images/')
    blog_user = models.ForeignKey(User, on_delete=models.CASCADE)

   # shows title of blogs in admin area
    def __str__(self):
        return self.title


   # limits post to 100 chars
    def summary(self):
        return self.post[:100]

   # adjust date time
    def date_only(self):
        return self.publication_date.strftime('%b %e %Y')
