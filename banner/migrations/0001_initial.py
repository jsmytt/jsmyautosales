# Generated by Django 2.1.4 on 2018-12-22 02:59

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
                ('BImage1', models.ImageField(blank=True, null=True, upload_to='listing')),
                ('BImage2', models.ImageField(blank=True, null=True, upload_to='listing')),
                ('BImage3', models.ImageField(blank=True, null=True, upload_to='listing')),
                ('BImage4', models.ImageField(blank=True, null=True, upload_to='listing')),
                ('BImage5', models.ImageField(blank=True, null=True, upload_to='listing')),
                ('BImage6', models.ImageField(blank=True, null=True, upload_to='listing')),
                ('BImage7', models.ImageField(blank=True, null=True, upload_to='listing')),
                ('BImage8', models.ImageField(blank=True, null=True, upload_to='listing')),
                ('BImage9', models.ImageField(blank=True, null=True, upload_to='listing')),
                ('BImage10', models.ImageField(blank=True, null=True, upload_to='listing')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
        ),
    ]
