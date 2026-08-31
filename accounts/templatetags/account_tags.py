from datetime import datetime, date
from django import template
from django.utils import timezone

register = template.Library()

@register.simple_tag
def days_on_site(date_joined):
    days = (timezone.now() - date_joined).days

    if 11 <= days <= 14:
        word = "днів"
    elif days % 10 == 1:
        word = "день"
    elif 2 <= days % 10 <= 4:
        word = "дні"
    else:
        word = "днів"

    return f'{days} {word}'
