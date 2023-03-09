from django.contrib import admin
from .models import Book,Comment


# Register your models here.





@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =  ['title',  'rating','publication_date']
    list_filter = ['title', ]
    search_fields = ['title', ]
    date_hierarchy =  'publication_date'
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'book', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']


