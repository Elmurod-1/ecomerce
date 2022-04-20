from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('chekout/', views.checkout, name='checkout'),

    path('updateitem/', views.updateItem, name='update_item'),
    path('processorder/', views.processOrder, name='processorder'),
]
