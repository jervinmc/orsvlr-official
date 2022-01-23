# Generated by Django 4.0.1 on 2022-01-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promoCode', models.CharField(blank=True, max_length=255, null=True, verbose_name='promoCode')),
                ('percentage', models.CharField(blank=True, max_length=255, null=True, verbose_name='percentage')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
