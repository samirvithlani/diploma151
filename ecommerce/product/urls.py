from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

path('products/',views.products),
path('register/',views.RegisterProductView.as_view()),
path('list/',views.ListProductView.as_view()),
    
]
