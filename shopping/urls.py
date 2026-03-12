from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_list, name='shopping_list'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('toggle/<int:item_id>/', views.toggle_purchased, name='toggle_purchased'),
]
