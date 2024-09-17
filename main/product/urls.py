from django.urls import path 
from . import views


urlpatterns = [

    path('product_list/',views.products,name='product'),
    path('add_product/',views.add_product,name='add_product')

]