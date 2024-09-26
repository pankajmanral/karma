from django.urls import path
from . import views


urlpatterns = [

    path('show-brand/',views.show_brand,name='show_brand'),
    path('add-brand/',views.AddBrand.as_view(),name='add_brand'),
    path('update-brand/<int:id>',views.UpdateBrand.as_view(),name='update_brand'),
    path('show-product/',views.show_product,name='show_product'),
    path('add-product/',views.AddProduct.as_view(),name='add_product'),
    path('update-product/<int:id>',views.UpdateProduct.as_view(),name='update_product'),
    path('show-product-style/',views.show_product_type,name='show_product_type'),
    path('add-product-type/',views.AddProductType.as_view(),name='add_product_type'),
    path('update-product-type/<int:id>',views.UpdateProductType.as_view(),name='update_product_type')

]