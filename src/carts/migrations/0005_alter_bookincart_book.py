# Generated by Django 3.2.3 on 2021-06-30 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20210623_2229'),
        ('carts', '0004_auto_20210630_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookincart',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='Книга'),
        ),
    ]
