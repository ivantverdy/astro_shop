from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_home, name='cart'),
    path('add/', views.cart_add, name='add'),
    path('delete/', views.cart_delete, name='delete'),
    path('update/', views.cart_update, name='update'),
]
