# Generated by Django 4.0.1 on 2022-02-14 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_book_promocode'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cancellation_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='cancellation_description'),
        ),
    ]
