from django.db import models

# Create your models here.
class product(models.Model):
             #module.Class  
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2,max_digits=10)