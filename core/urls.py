from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from .views import frontpage, shop, signup, myaccount, editmyaccount, price_filter


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop', shop, name='shop'),
    path('shop/price-filter', price_filter, name='price_filter'),
    path('signup', signup, name='signup'),
    path('login', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit', editmyaccount, name='editmyaccount'),
    
   
] 
