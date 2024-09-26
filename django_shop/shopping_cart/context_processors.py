from .cart import Cart


# context processor so the cart will work on all pages
def cart(request):
    return {'cart': Cart(request)}
