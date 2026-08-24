from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.products_list, name="product_list"),
    path('category/<slug:category_slug>/', views.products_list, name="product_list_by_category")
]