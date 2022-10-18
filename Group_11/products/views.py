from django.shortcuts import render
#from products.models import products

# Create your views here.

def products(request):  
    return render(request, "products/products.html")




