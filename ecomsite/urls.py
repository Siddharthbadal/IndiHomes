from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import core.urls
import product.urls
import cart.urls
import order.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core.urls)),
    path('', include(product.urls)),
    path('', include(cart.urls)),
    path('', include(order.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
