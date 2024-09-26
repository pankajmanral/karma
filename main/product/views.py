from django.shortcuts import render,redirect,get_object_or_404
from . models import Product,Brand,Style
from django.views import View
from . forms import ProductForm,BrandForm,ProductTypeForm

# Brand CRUD
def show_brand(request):
    data = Brand.objects.all()
    return render(request,'product/show_brand.html',{'brand':data})

class AddBrand(View):
    def get(self,request):
        form = BrandForm()
        return render(request,'product/add_brand.html',{'form':form})
    def post(self,request):
        form = BrandForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('show_brand')
        return render(request,'product/add_brand.html',{'form':form})
    
class UpdateBrand(View):
    def get(self,request,id):
        data = get_object_or_404(Brand,id=id)
        form = BrandForm(instance=data)
        return render(request,'product/update_brand.html',{'form':form,'data':data})
    def post(self,request,id):
        data = get_object_or_404(Brand,id=id)
        form = BrandForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('show_brand')
        return render(request,'product/add_brand.html',{'form':form})
    
# Product CRUD 
def show_product(request):
    data = Product.objects.all()
    return render(request,'product/show_product.html',{'product':data})   

class AddProduct(View):
    def get(self,request):
        form = ProductForm()
        return render(request,'product/add_product.html',{'form':form})
    def post(self,request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_product')
        return render(request,'product/add_product.html',{'form':form})
    
class UpdateProduct(View):
    def get(self,request,id):
        data = get_object_or_404(Product,id=id)
        form = ProductForm(instance=data)
        return render(request,'product/update_product.html',{'form':form})
    
    def post(self,request,id):
        data = get_object_or_404(Product,id=id)
        form = ProductForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('show_product')
        return render(request,'product/update_product.html',{'form':form})
        
# Show Product Type 
def show_product_type(request):
    data = Style.objects.all()
    return render(request,'product/show_product_type.html',{'type':data})

class AddProductType(View):
    def get(self,request):
        form = ProductTypeForm()
        return render(request,'product/add_product_type.html',{'form':form})
    def post(self,request):
        form = ProductTypeForm(request.POST)
        form.save()
        if form.is_valid():
            return redirect('show_product_type')
        return render(request,'product/add_product_type.html',{'form':form})
               
class UpdateProductType(View):
    def get(self,request,id):
        data = get_object_or_404(Style,id=id)
        form = ProductTypeForm(instance=data)
        return render(request,'product/update_product_type.html',{'form':form})
    def post(self,request,id):
        data = get_object_or_404(Style,id=id)
        form = ProductTypeForm(request.POST,instance=data,)
        form.save()
        if form.is_valid():
            return redirect('show_product_type')
        return render(request,'product/update_product_type.html',{'form':form})
    
    