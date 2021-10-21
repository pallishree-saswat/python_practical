from django.urls import path

from api import views

urlpatterns = [
    path('getAll/',views.ShowAll),
    path('getOne/<int:pk>',views.ProductDetail),
    path('addproduct/',views.AddProduct),
    path('editProduct/<int:pk>',views.UpdateProduct),
    path('deleteProduct/<int:pk>',views.Deleteproduct),
]