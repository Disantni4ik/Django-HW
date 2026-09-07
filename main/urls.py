from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.product_list, name="product_list"),
    path('contact/', views.contact_view, name='contact'),
    path('category/<slug:category_slug>/', views.product_list, name="product_list_by_category"),
    path('category/<int:id>/<slug:slug>/', views.product_detail, name="product_detail.html"),
    path('/cart/', views.cart_detail, name='cart_detail'),
    path('/cart/add/<int:product_id>', views.cart_add, name='cart_add'),
    path('/cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
]