from django.contrib import admin
from django.utils.html import format_html

from main.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_active', 'image_tag')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return format_html('<span>Немає зображення</span>')

    image_tag.short_description = "Зображення"

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}