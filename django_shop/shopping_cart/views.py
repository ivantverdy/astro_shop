from django.shortcuts import render


def cart_home(request):
    return render(request, 'cart_home.html', {})


def cart_add(request):
    pass


def cart_delete(request):
    pass


def cart_update(request):
    pass
