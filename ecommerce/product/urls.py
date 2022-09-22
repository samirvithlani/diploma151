from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

path('products/',views.products),
path('register/',views.RegisterProductView.as_view(),name="register"),
path('list/',views.ListProductView.as_view()),
path('delete/<int:pk>',views.DeleteProductView.as_view(),name="delete_product"),
path('productdetail/<int:pk>',views.DetailProductView.as_view(),name="product_detail"),
path('update/<int:pk>',views.UpdateProductView.as_view(),name="update_product"),
    
]
