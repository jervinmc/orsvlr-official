# Generated by Django 4.0.1 on 2022-03-29 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_book_cancellation_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_reschedule',
            field=models.DateField(blank=True, null=True, verbose_name='date_reschedule'),
        ),
        migrations.AddField(
            model_name='book',
            name='reason_reschedule',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='reason_reschedule'),
        ),
    ]
