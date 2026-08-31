from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.product_list, name="product_list"),
    path('contact/', views.contact_view, name='contact'),
    path('category/<slug:category_slug>/', views.product_list, name="product_list_by_category"),
    path('category/<int:id>/<slug:slug>/', views.product_detail, name="product_detail.html")
]