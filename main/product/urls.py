from django.urls import path 
from . import views


urlpatterns = [

    path('product_list/',views.products,name='product'),
    path('add_product/',views.add_product,name='add_product'),
    path('product_types/',views.product_types,name='product_types'),
    path('update_product/<int:id>/',views.update_product,name='update_product'),
    path('confirm_delete/<int:id>/',views.confirm_product,name='confirm_delete'),
    path('delete_productType/<int:id>/',views.delete_productType,name='delete_productType'),

]