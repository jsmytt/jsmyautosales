from django.db import models
from ckeditor.fields import RichTextField

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Car(models.Model):
    type = models.CharField(max_length=25, choices=[('New', 'New Vehicle'), ('Used', 'Used Vehicle'), ('Lease', 'Rental Vehicle'),('faq', 'FAQ')], default='New', verbose_name='Listing Type')
    title = models.CharField(max_length=500, verbose_name='Title of Vehicle Listing')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Price of Vehicle in Dollar Amount')
    body = RichTextField(verbose_name='Description of Vehicle')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='SLUG: Your URL will have this in the address')
    publish = models.BooleanField(default=True)
    sold = models.CharField(max_length=10,verbose_name='Sold Y/N',choices=[('Sale', 'For Sale'), ('Solded', 'Sold')], default='Sale')
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    object = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Car Listing Entry"
        verbose_name_plural = "Car Listing Entries"
        ordering = ["-created"]

class CarImg(models.Model):
    LImage = models.ImageField(null=True, blank=False, upload_to="listing")
    car = models.ForeignKey(Car,default='car', on_delete=models.CASCADE , related_name = 'cari')
    MainImage = models.BooleanField(default = False)


class faqath(models.Model):
    attachment = models.FileField(null=True, blank=False, upload_to="listing/ath")
    car = models.ForeignKey(Car, default='car', on_delete=models.CASCADE, related_name='carath')

