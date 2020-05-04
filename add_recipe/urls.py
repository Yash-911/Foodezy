"""Foodezy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addrecipe',views.addrecipe,name="addrecipe"),
    path('add_submitted_recipe',views.add_submitted_recipe,name="add_submitted_recipe"),
    path('viewrecipe',views.viewrecipe,name="viewrecipe"),
    path('add_cart/<recipe_name>/',views.add_cart,name="add_cart"),
    path('view_cart',views.view_cart,name="view_cart"),
    path('delfrm_cart/<recipe_name>',views.delfrm_cart,name="delfrm_cart"),
    path('filtering/<type>',views.filtering,name="filtering"),
    path('viewpage/<recipe_name>',views.viewpage,name="viewpage"),
    path('checkout', views.checkout, name="checkout"),
    path('add_quantity/<recipe_name>', views.add_quantity, name="add_quantity"),
    path('sub_quantity/<recipe_name>', views.sub_quantity, name="sub_quantity"),
    path('add_checkout_details', views.add_checkout_details, name="add_checkout_details"),
    path('payment', views.payment, name="payment"),
    path('search', views.search, name="search"),

]
