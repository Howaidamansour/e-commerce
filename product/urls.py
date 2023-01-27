from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:slug>', views.product_detiels, name='product_detail'),
    path('<slug:category_slug>', views.product_list, name='product_by_category'),
]
