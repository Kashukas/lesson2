# Generated by Django 3.2.3 on 2021-06-24 22:39

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200, verbose_name='Страна')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
                ('postcode', models.IntegerField(verbose_name='Почтовый индекс')),
                ('address1', models.TextField(verbose_name='Адрес 1')),
                ('address2', models.TextField(default='---', verbose_name='Адрес 2')),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('phone', models.CharField(max_length=300, verbose_name='Телефон')),
                ('addit_info', models.TextField(default='---', verbose_name='Адрес 2')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='customer_address', to='users.useraddress', verbose_name='Домашний адрес')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]