# Generated by Django 4.0 on 2022-01-16 00:30

import book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_book_subtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='uploads/book.png', upload_to=book.models.nameFile, verbose_name='image'),
        ),
    ]
