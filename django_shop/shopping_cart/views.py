from django.shortcuts import render, get_object_or_404
from .cart import Cart
from astro_shop.models import Product
from django.http import JsonResponse


def cart_home(request):
    return render(request, 'cart_home.html', {})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':  # in js action = lowercase post
        # get from button id of product
        product_id = request.POST.get('product_id')
        # look for product in db
        product = get_object_or_404(Product, pk=product_id)
        # save
        cart.add(product=product)
        # return response
        response = JsonResponse({'product name: ': product.name})
        return response


def cart_delete(request):
    pass


def cart_update(request):
    pass
