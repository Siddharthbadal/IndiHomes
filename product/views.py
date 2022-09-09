from django.shortcuts import get_object_or_404, render
from .models import Product


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:3]
    return render(request, 'product/product.html', {'product':product, 'related_products':related_products})
