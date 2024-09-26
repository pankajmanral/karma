from django.forms import ModelForm
from . models import Product,Brand,Style

class BrandForm(ModelForm):
    class Meta():
        model = Brand
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta():
        model = Product
        fields = '__all__'

class ProductTypeForm(ModelForm):
    class Meta():
        model = Style
        fields = '__all__'