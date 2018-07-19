from django.db import models

# Create your models here.
class ClientsDatabase(models.Model):
    NAME = models.CharField(max_length=50,blank=True)
    CONTACT = models.CharField(max_length=50,blank=True)
    OCCUPATION = models.CharField(max_length=100, blank=True)
    CLIENT_NO = models.IntegerField()
    POLICY_NO = models.IntegerField()
    POLICY_TYPE = models.CharField(max_length=100,blank=True)
    POLICY_PROPERTIES = models.CharField(max_length=100,blank=True)
    ISSUE_DATE = models.DateField()
    REVIEW_DATE = models.DateField()
    DOB = models.DateField()
    ADDRESS = models.TextField(max_length=1000,blank=True)
    PREMIUM_AMOUNT = models.FloatField()
    MODE_OF_PAYMENT = models.CharField(max_length=100,blank=True)
    PDF = models.FileField(upload_to='pdf/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.NAME