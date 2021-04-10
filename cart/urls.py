from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='welcome'),
    path('create/', views.createProduct, name='create'),
    path('setCookie/', views.setCookie, name='setCookie'),
    # path('ajaxview/', views.AjaxView.as_view(), name='ajaxview'),
    # path('ajaxview/create/', views.CreateCrudUser.as_view(), name='create'),
    path('template/', views.template, name='template'),
    path('ajax-posting/', views.ajax_posting, name='ajax_posting'),
    path('MultipleForm/', views.MultipleForm, name='MultipleForm'),
    path('setSession/', views.setSession, name='setSession'),
    path('update/<str:pk>/', views.updateProduct, name='update'),
    path('product/<str:pk>', views.show_products, name='show_products'),
    path('order/<str:pk>/', views.show_orders, name='show_orders'),
    path('items/<str:pk>/', views.show_orderItems, name='items'),

]