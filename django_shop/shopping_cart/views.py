from django.shortcuts import render, get_object_or_404
from .cart import Cart
from astro_shop.models import Product
from django.http import JsonResponse


def cart_home(request):
    cart = Cart(request)
    cart_products = cart.get_products_with_quantities()
    total = cart.get_total()
    quantity_range = range(1, 11)

    return render(request, 'cart_home.html', {
        'cart_products': cart_products,
        'total': total,
        'quantity_range': quantity_range,
    })


def cart_add(request):
    # this step does not create a new cart from scratch but instead retrieves the existing cart from the session
    cart = Cart(request)
    if request.POST.get('action') == 'post':  # in js action = lowercase post
        # get a product from button id of product
        product_id = request.POST.get('product_id')

        # look for product in db
        product = get_object_or_404(Product, pk=product_id)
        # save
        cart.add(product=product)

        cart_quantity = cart.__len__()
        # return response
        # response = JsonResponse({'product name: ': product.name})
        response = JsonResponse({'cart_qty': cart_quantity})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, pk=product_id)

        cart.delete(product=product)


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, pk=product_id)
        quantity = int(request.POST.get('quantity'))

        cart.update(product=product, quantity=quantity)
        total = cart.get_total()

        return JsonResponse({'total': total})