from django.shortcuts import render,redirect,get_object_or_404
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
        name = request.POST.get('name')
        price = request.POST.get('price')
                              #database name = created variable
        product.objects.create(name = name , price = price)

        return render(request,'product/product_list.html')
    elif request.method == "GET":
        return render(request,'product/add_product.html')
    
def update_product(request,id):
    # product = product.objects.get(id = id)
    pro = get_object_or_404(product,id=id)
    if request.method == "POST":
        pro.name = request.POST.get('name')
        pro.price = request.POST.get('price')
        pro.save()
        return redirect('product')
        # POST method is used to get the data from the form 

    elif request.method == 'GET':
        print(pro.name )
        return render(request,'product/update_product.html',{'pro':pro})

        # GET method is used to redirect to the update page