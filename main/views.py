from django.shortcuts import render, get_object_or_404

from main.models import Product, Category


def products_list(request, category_slug=None):
    products = Product.objects.all()
    categories = Category.objects.all()
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'title': "Список продуктів",
        'products': products,
        'categories': categories,
        'category': category,
    }

    return render(request, 'main/product_list.html', context)
