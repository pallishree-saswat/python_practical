from django.urls import path
from helloworld import views

urlpatterns =[
    path('',views.index),
    path('home/',views.home)
]