# Generated by Django 2.1.4 on 2018-12-22 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0009_auto_20181222_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='LImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
