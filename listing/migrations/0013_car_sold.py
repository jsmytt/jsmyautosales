# Generated by Django 2.1.2 on 2018-12-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0012_auto_20181228_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='sold',
            field=models.BooleanField(choices=[('Sale', 'For Sale'), ('Sold', 'Sold')], default=True, verbose_name='Sold Y/N'),
        ),
    ]
