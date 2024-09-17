from django.shortcuts import render
from .models import product
# Create your views here.

def products(request):
    data = product.objects.all()
    context = {
        'products' : data
    }
    return render(request,'product/product_list.html',context)


def add_product(request):
    if request.method == "POST":
        return render(request,'product/product_list.html')
    elif request.method == "GET":
        return render(request,'product/add_product.html')