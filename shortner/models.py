from django.db import models
#after edit or add or delete a model :  
#makemigrations
#migrate
# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10 ,blank=True, null=True) #views does it