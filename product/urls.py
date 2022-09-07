from django.urls import path
from product.views import product


urlpatterns = [
    path('shop/<slug:slug>/', product, name='product'),
   
]
