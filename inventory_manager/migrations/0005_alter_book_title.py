# Generated by Django 4.1.3 on 2022-11-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manager', '0004_alter_book_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='Enter book title', max_length=500),
        ),
    ]
