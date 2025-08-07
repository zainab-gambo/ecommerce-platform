from django.urls import path
from . import views

urlpatterns = [
path('', views.product_list, name='product-list'),
path('', views.home, name='home'),             # root page
path('all/', views.product_list, name='product_list'),  
path('category/<str:category_name>/', views.product_list_by_category, name='category_view'),

]
