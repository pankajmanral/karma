from django.db import models

# Create your models here.
class product(models.Model):
             #module.Class  
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    def __str__(self) -> str :
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=25)


class product_type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)
    desc = models.TextField(max_length=50)
    def __str__(self) -> str:
        return self.type_name
    
