# Generated by Django 2.1.2 on 2018-12-28 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0004_auto_20181228_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='BImage1',
            field=models.ImageField(null=True, upload_to='banner', verbose_name='Banner Image 1'),
        ),
    ]