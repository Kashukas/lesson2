# Generated by Django 3.2.3 on 2021-07-03 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(default='---', max_length=200, verbose_name='Страна'),
        ),
    ]
