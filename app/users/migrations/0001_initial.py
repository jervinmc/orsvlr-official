# Generated by Django 4.0.1 on 2022-02-02 12:31

from django.db import migrations, models
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(blank=True, default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_joined')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='name')),
                ('firstname', models.CharField(blank=True, default='', max_length=255, verbose_name='firstname')),
                ('lastname', models.CharField(blank=True, default='', max_length=255, verbose_name='lastname')),
                ('middlename', models.CharField(blank=True, default='', max_length=255, verbose_name='middlename')),
                ('username', models.CharField(blank=True, default='', max_length=255, verbose_name='username')),
                ('gender', models.CharField(blank=True, default='', max_length=255, verbose_name='gender')),
                ('password', models.CharField(blank=True, default='', max_length=255, verbose_name='password')),
                ('email', models.CharField(blank=True, default='', max_length=255, unique=True, verbose_name='email')),
                ('account_type', models.CharField(blank=True, default='', max_length=255, verbose_name='account_type')),
                ('image', models.ImageField(default='uploads/users_placeholder.png', upload_to=users.models.nameFile, verbose_name='image')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
