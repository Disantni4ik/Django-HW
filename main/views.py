from django.shortcuts import render

from main.models import Product

def products_list(request):
    products = Product.objects.all()

    context = {'title': "Список продуктів",
               'products': products}

    return render(request, 'main/products_list.html', context)
