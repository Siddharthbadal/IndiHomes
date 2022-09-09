from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .cart import Cart
from product.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)  
    return render(request, 'cart/menu_cart.html', {'cart':cart})


@csrf_exempt
def cart(request):
    return render(request, 'cart/cart.html')


@csrf_exempt
def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
        
    else:
        cart.add(product_id, -1, True)
        

    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)
    
    if quantity:
        quantity = quantity['quantity']

        item = {
            'product': {
                'id': product_id,
                'name': product.name,
                'image': product.image,
                'get_thumbnail': product.get_thumbnail(),
                'price': product.price
            },
            'total_price': (quantity * product.price),
            'quantity': quantity,
        }
    else:
        item = None

    response = render(request, 'cart/partials/cart_item.html', {'item':item})
    response['HX-Trigger'] = 'update-menu-cart'
    return response


@csrf_exempt
@login_required
def checkout(request):
    cart = Cart(request)
    if len(cart) < 1:
        return redirect('shop')
    return render(request, 'cart/checkout.html')

def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')

def hx_cart_total(request):
    return render(request, 'cart/partials/cart_total.html')

def success(request):
    return render(request, 'cart/success.html')