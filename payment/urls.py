from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('order/', views.order, name='order'),
    path('cart/', views.cart, name='cart'),
    path('wish/', views.wish, name='wish'),
    path('complete/', views.complete, name='complete'),
    path('error/', views.error, name='error'),
]
