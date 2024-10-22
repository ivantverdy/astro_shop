from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.register_user, name='signup'),
    path('product/<int:pk>', views.single_product, name='product'),
    path('update_user/', views.update_user, name='update_user'),
]
