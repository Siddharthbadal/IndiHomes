from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from .views import frontpage, shop, signup, myaccount, editmyaccount


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop', shop, name='shop'),
    path('signup', signup, name='signup'),
    path('login', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit', editmyaccount, name='editmyaccount'),
    
   
] 
