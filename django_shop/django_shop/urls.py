from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('astro_shop.urls')),
    path('cart/', include('shopping_cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
