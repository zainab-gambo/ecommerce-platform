from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()[:8]  # Show latest 8
    return render(request, 'products/home.html', {
        'products': products,
        'product_categories': Product.CATEGORY_CHOICES
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'storefront/product_detail.html', {'product': product})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_list_by_category(request, category_name):
    products = Product.objects.filter(category=category_name)
    return render(request, 'products/product_list.html', {'products': products})
