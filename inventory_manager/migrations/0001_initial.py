# Generated by Django 4.1.3 on 2022-11-20 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter first name of author.', max_length=100)),
                ('last_name', models.CharField(help_text='Enter last name of author.', max_length=100)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre.', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SupportTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('topic', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter book title', max_length=200)),
                ('synopsis', models.TextField(help_text='A summary of the book content.', max_length=3000)),
                ('isbn', models.CharField(help_text='13-digit ISBN', max_length=13, unique=True, verbose_name='ISBN')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('quantity', models.IntegerField(help_text='Enter amount in stock.', verbose_name='Quantity')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory_manager.author')),
                ('genre', models.ForeignKey(help_text='Select Genre', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory_manager.genre')),
            ],
        ),
    ]