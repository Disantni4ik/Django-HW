from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from main.cart import Cart
from main.forms import ContactForm
from main.models import Product, Category


def product_list(request, category_slug=None):
    products = Product.objects.select_related('category').filter(is_active=True)
    categories = Category.objects.all()
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    sort = request.GET.get('sort', 'new')

    if sort == 'new':
        products = products.order_by('-created_at')
    elif sort == 'old':
        products = products.order_by('created_at')
    elif sort == 'popular':
        products = products.order_by('-views', '-created_at')
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')

    context = {
        'title': "Список продуктів",
        'products': products,
        'categories': categories,
        'category': category,
        'current_sort': sort,
    }

    return render(request, 'main/product_list.html', context)

def product_detail(request, id ,slug):
    product = get_object_or_404(
        Product.objects.select_related('category'),
        id=id,
        slug=slug,
        is_active=True
    )

    Product.objects.filter(id=id).update(views=F('views') + 1)
    product.refresh_from_db(fields=['views'])

    related_products = Product.objects.filter(category=product.category, is_active=True).exclude(id=product.id).select_related('category')[:4]

    context = {
        'title': product.name,
        'product': product,
        'related_products': related_products
    }

    return render(request, 'main/product_detail.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            email_subject = f"Нове повідомлення: {subject}"
            email_message = f"Отримано нове звернення через контактну форму сайту.\n\n" \
                            f"Від кого: {name}\n" \
                            f"Email відправника: {email}\n\n" \
                            f"Текст повідомлення:\n{message}"

            try:
                send_mail(
                    subject=email_subject,
                    message=email_message,
                    from_email=email,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )

                messages.success(
                    request,
                    "Дякуємо! Ваше повідомлення успішно надіслано на пошту адміністратора."
                )
                return redirect('main:contact')

            except Exception as e:
                messages.error(
                    request,
                    "Виникла помилка при відправленні листа. Будь ласка, спробуйте пізніше."
                )
                print(f"Помилка відправлення пошти: {e}")

            return redirect('main:contact')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'title': 'Відправити повідомлення', 'form': form})

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    override = request.POST.get('override', False)

    if isinstance(override, str):
        override = override.lower() in ['true', '1', 'yes']

    cart.add(product=product, quantity=quantity, override_quantity=override)
    return redirect('main:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('main:cart_detail')

def cart_detail(request):
    return render(request, 'main/cart_detail.html', {
        'title': 'Кошик покупця'
    })