# Generated by Django 3.2.3 on 2021-06-20 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manuals', '0003_alter_serie_books_quantity'),
        ('books', '0003_alter_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author_books', to='manuals.author', verbose_name='Автор'),
        ),
    ]
