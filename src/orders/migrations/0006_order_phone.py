# Generated by Django 3.2.3 on 2021-07-14 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=291245677, max_length=15, verbose_name='Телефон'),
            preserve_default=False,
        ),
    ]
