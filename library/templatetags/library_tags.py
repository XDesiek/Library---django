from django import template
from ..models import Book
from django.db.models import Count



register = template.Library()



@register.simple_tag
def book_count():
    return Book.objects.count()