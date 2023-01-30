from django.db import models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)
    username=models.CharField(max_length=32,unique=True)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=32)
    bio=models.CharField(max_length=512,blank=True)
    class Meta:
        indexes = [models.Index(fields=['username'])]
    def __str__(self):
        return self.username



class Book(models.Model):

    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='books')
    title=  models.TextField(max_length=63)
    publication_date= models.DateField(default=timezone.now)
    # author = models.TextField(max_length=63)
    slug = models.SlugField(max_length=63,unique_for_date="publication_date")
    desc=  models.TextField()
    rating = models.IntegerField()
    tags=TaggableManager()
    

    class Meta:
        ordering = ['title']
        indexes = [models.Index(fields=['title'])]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse(
            "library:book_detail",
            args=[self.publication_date.year, self.publication_date.month, self.publication_date.day, self.slug]
            )


class Comment(models.Model):
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    def __str__(self):
        return f'Comment by {self.name} on {self.book}'
















# class Author(models.Model):
#     name=  models.TextField(max_length=16)
#     secondname=  models.TextField(max_length=32)
#     brith_date= models.DateField()
#     desc=  models.TextField()

    
#     class Meta:
#         indexes = [models.Index(fields=[['second name'],["name"]])]

#     def __str__(self) -> str:
#         return (f"{self.name} {self.secondname}")