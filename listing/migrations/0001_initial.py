# Generated by Django 2.1.2 on 2019-01-17 05:07

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('New', 'New Vehicle'), ('Used', 'Used Vehicle'), ('Lease', 'Rental Vehicle'), ('faq', 'FAQ')], default='New', max_length=25, verbose_name='Listing Type')),
                ('title', models.CharField(max_length=500, verbose_name='Title of Vehicle Listing')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price of Vehicle in Dollar Amount')),
                ('body', ckeditor.fields.RichTextField(verbose_name='Description of Vehicle')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='SLUG: Your URL will have this in the address')),
                ('publish', models.BooleanField(default=True)),
                ('sold', models.CharField(choices=[('Sale', 'For Sale'), ('Sold', 'Sold')], default='Sale', max_length=10, verbose_name='Sold Y/N')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Car Listing Entry',
                'verbose_name_plural': 'Car Listing Entries',
                'ordering': ['-created'],
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CarImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LImage', models.ImageField(null=True, upload_to='listing')),
                ('MainImage', models.BooleanField(default=False)),
                ('car', models.ForeignKey(default='car', on_delete=django.db.models.deletion.CASCADE, related_name='cari', to='listing.Car')),
            ],
        ),
    ]
