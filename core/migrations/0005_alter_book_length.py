# Generated by Django 4.0.3 on 2022-03-17 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_author_genre_book_cover_book_created_at_book_length_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='length',
            field=models.IntegerField(help_text='The page count of the book.'),
        ),
    ]
