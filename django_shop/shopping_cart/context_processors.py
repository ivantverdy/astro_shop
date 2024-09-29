from .cart import Cart


# context processor so the cart will work on all pages
def cart(request):
    # basically Cart(request) initializes a new empty cart when a new user enters a website
    return {'cart': Cart(request)}
