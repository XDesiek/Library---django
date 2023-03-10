# Generated by Django 4.1.4 on 2023-01-01 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_slug_alter_book_author_alter_book_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=63, unique_for_date='publication_date'),
        ),
    ]
