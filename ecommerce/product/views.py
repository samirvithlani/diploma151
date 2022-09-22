from django.shortcuts import render

from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView

from .models import Product

# Create your views here.
def products(request):
    return render(request,"products/products.html")


class RegisterProductView(CreateView):
    model  = Product
    fields = "__all__"
    template_name = "products/product_register.html"
    success_url = "/product/list/"
    
class ListProductView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = 'products'    

class DeleteProductView(DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    success_url = "/product/list/"   
    
class DetailProductView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"  

class UpdateProductView(UpdateView):
    model = Product
    template_name = "products/product_update.html"
    context_object_name = "product"
    fields = "__all__"
    success_url = "/product/list/"