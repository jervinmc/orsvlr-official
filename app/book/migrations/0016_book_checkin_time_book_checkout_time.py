# Generated by Django 4.0.1 on 2022-05-29 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_book_ad_discount_book_ad_discount_total_book_ad_ons_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='checkin_time',
            field=models.DateField(blank=True, null=True, verbose_name='checkin_time'),
        ),
        migrations.AddField(
            model_name='book',
            name='checkout_time',
            field=models.DateField(blank=True, null=True, verbose_name='checkout_time'),
        ),
    ]
