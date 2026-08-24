from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:product_list_by_category", args=[self.slug])

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг для URL')
    image = models.ImageField(upload_to='products/%Y%m/%d', blank=True, verbose_name='Зображення')
    views = models.IntegerField(default=0, verbose_name='Кількість переглядів')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"

    def __str__(self):
        return f'{self.name} | {self.created_at}'

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.slug])