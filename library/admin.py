from django.contrib import admin
from .models import Book,Comment,User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    list_filter = ['username', 'first_name',"last_name"]
    search_fields = ['username','first_name', 'last_name']



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =  ['title', 'author', 'rating','publication_date']
    list_filter = ['title', 'author']
    search_fields = ['title', 'author']
    date_hierarchy =  'publication_date'
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'book', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']


