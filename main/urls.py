from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.products_list, name="products_list")
]