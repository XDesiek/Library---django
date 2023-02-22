from django import template
from ..models import Book
from django.db.models import Count



register = template.Library()



@register.simple_tag
def book_count():
    return Book.objects.count()


@register.inclusion_tag('library/book/best_books.xhtml')
def show_best_books(count=5):
    best_books = Book.objects.order_by('-rating')[:count]
    return {'best_books': best_books}


@register.simple_tag()
def get_most_commented_books(count=5):
        return Book.objects.annotate(total_comments = Count("comments")).order_by('-total_comments')[:count]
