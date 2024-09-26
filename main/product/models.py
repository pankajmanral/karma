# from django.db import models

# # Create your models here.
# class product(models.Model):
#              #module.Class  
#     name = models.CharField(max_length=20)
#     price = models.DecimalField(decimal_places=2,max_digits=10)
#     def __str__(self) -> str :
#         return self.name

# class Category(models.Model):
#     name = models.CharField(max_length=25)
#     def __str__(self):
#         return self.name


# class product_type(models.Model):
#     id = models.AutoField(primary_key=True)
#     type_name = models.CharField(max_length=20)
#     desc = models.TextField(max_length=50)
#     def __str__(self) -> str:
#         return self.type_name
    
# class Category(models.Model):
#     name = models.CharField(max_length=25)

# class ProductType(models.Model):
#     id  = models.IntegerField(models.BigAutoField,primary_key=True,auto_created=True)
#     name = models.CharField(max_length=25)
#     description = models.TextField(verbose_name='desc')
#     def __str__(self)->str:
#         return self.name

# python manage.py makemigrations
# python manage.py migrate
# # for i in Product.objects.filter(price__in = ( 176.43, 250.60,176.44,150)):
#     print(f'{str(i.id).center(4,' ')} | {i.name.center(20,' ' )} | {i.price}')




from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='brands/', null=True, blank=True)
    class Meta:
        db_table = 'Brand'
    def __str__(self):
        return f'{self.name} | {self.description}'

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    description = models.TextField(default='default description')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,default=0)

    # image = models.ImageField(upload_to='products/')
    def __str__(self) -> str:
        return f'{self.name} : {self.brand.name} '
    class Meta:
        db_table = 'Product'

class Shoe(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE,default=0)
    class Meta:
        db_table='Shoe'
    def __str__(self):
        return f'{self.product.name} : ₹{self.product.price:.2f}'

class Style(models.Model):
    color = models.CharField(max_length=20)
    size = models.IntegerField(default=7)
    type = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    # shoe = models.ManyToManyField(Shoe,through='ShoeStyle')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,default=1)
    class Meta:
        unique_together = ('color', 'size','material')
        db_table = 'Style'
    def __str__(self):
        return f'Brand : {self.brand.name} | Color : {self.color} | Type : {self.type} | Material : {self.material}'

class ShoeStyle(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE,default=0)
    style = models.ForeignKey(Style, on_delete=models.CASCADE,default=0)
    class Meta:
        unique_together = (('shoe', 'style'),)
        db_table = 'ShoeStyle'
    def __str__(self):
        return f'{self.shoe} | {self.style}'
