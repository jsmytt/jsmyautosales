# Generated by Django 2.1.4 on 2019-01-05 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_auto_20190103_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='carimg',
            name='MainImage',
            field=models.BooleanField(default=True),
        ),
    ]
