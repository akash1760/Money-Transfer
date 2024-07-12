from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('customers/', views.customers_list, name='customers_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/<int:pk>/transfer/', views.transfer_money, name='transfer_money'),
]
