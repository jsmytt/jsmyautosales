# Generated by Django 2.1.2 on 2018-12-28 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0003_banner_blink1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='BImage10',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='BImage6',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='BImage7',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='BImage8',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='BImage9',
        ),
        migrations.AddField(
            model_name='banner',
            name='Blink2',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='Banner Link 2'),
        ),
        migrations.AddField(
            model_name='banner',
            name='Blink3',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='Banner Link 3'),
        ),
        migrations.AddField(
            model_name='banner',
            name='Blink4',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='Banner Link 4'),
        ),
        migrations.AddField(
            model_name='banner',
            name='Blink5',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='Banner Link 5'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='BImage1',
            field=models.ImageField(blank=True, null=True, upload_to='banner', verbose_name='Banner Image 1'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='BImage2',
            field=models.ImageField(blank=True, null=True, upload_to='banner', verbose_name='Banner Image 2'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='BImage3',
            field=models.ImageField(blank=True, null=True, upload_to='banner', verbose_name='Banner Image 3'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='BImage4',
            field=models.ImageField(blank=True, null=True, upload_to='banner', verbose_name='Banner Image 4'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='BImage5',
            field=models.ImageField(blank=True, null=True, upload_to='banner', verbose_name='Banner Image 5'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='Blink1',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='Banner Link 1'),
        ),
    ]
