from django.urls import path 
from . import views
app_name = "products"

urlpatterns = [
    path('' , views.products , name="products"),
    path('our/' , views.our , name="our"),
    path('products_detail/<slug>/', views.products_details , name="products_detail"),
    path('add_to_cart/<slug>/' , views.add_to_cart , name="add_to_cart"),
]

