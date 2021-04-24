from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='welcome'),
    path('create/', views.createProduct, name='create'),
    path('multiclick/', views.multi_click, name='multiclick'),
    path('createOrder/', views.createOrder, name='createOrder'),
    path('template/', views.template, name='template'),
    path('ajaxcall/', views.ajaxcall, name='ajaxcall'),
    path('ajax-posting/', views.ajax_posting, name='ajax_posting'),
    path('MultipleForm/', views.MultipleForm, name='MultipleForm'),
    path('update/<str:pk>/', views.updateProduct, name='update'),
    path('product/<str:pk>', views.show_products, name='show_products'),
    path('order/<str:pk>/', views.show_orders, name='show_orders'),
    path('items/<str:pk>/', views.show_orderItems, name='items'),
    path('createpdf/<str:pk>/', views.createpdf, name='createpdf'),



]