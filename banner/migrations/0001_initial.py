# Generated by Django 2.1.2 on 2019-01-05 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BImage1', models.ImageField(null=True, upload_to='banner', verbose_name='Banner Image 1')),
                ('Blink1', models.URLField(blank=True, max_length=100, null=True, verbose_name='Banner Link 1')),
                ('BImage2', models.ImageField(null=True, upload_to='banner', verbose_name='Banner Image 2')),
                ('Blink2', models.URLField(blank=True, max_length=100, null=True, verbose_name='Banner Link 2')),
                ('BImage3', models.ImageField(null=True, upload_to='banner', verbose_name='Banner Image 3')),
                ('Blink3', models.URLField(blank=True, max_length=100, null=True, verbose_name='Banner Link 3')),
                ('BImage4', models.ImageField(null=True, upload_to='banner', verbose_name='Banner Image 4')),
                ('Blink4', models.URLField(blank=True, max_length=100, null=True, verbose_name='Banner Link 4')),
                ('BImage5', models.ImageField(null=True, upload_to='banner', verbose_name='Banner Image 5')),
                ('Blink5', models.URLField(blank=True, max_length=100, null=True, verbose_name='Banner Link 5')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
        ),
    ]
