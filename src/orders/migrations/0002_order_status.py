# Generated by Django 3.2.3 on 2021-06-30 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manuals', '0004_status'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='manuals.status', verbose_name='Статус заказа'),
        ),
    ]
