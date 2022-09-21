from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import Product

# Create your views here.
def products(request):
    return render(request,"products/products.html")


class RegisterProductView(CreateView):
    model  = Product
    fields = "__all__"
    template_name = "products/product_register.html"
    success_ur ="/"
    
class ListProductView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = 'products'    
    