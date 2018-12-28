from django.db import models

# Create your models here.
class banner(models.Model):
    BImage1 = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="Banner Image 1")
    Blink1 = models.URLField(max_length=100, null=True, blank=True, verbose_name="Banner Link 1")
    BImage2 = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="Banner Image 2")
    Blink2 = models.URLField(max_length=100, null=True, blank=True, verbose_name="Banner Link 2")
    BImage3 = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="Banner Image 3")
    Blink3 = models.URLField(max_length=100, null=True, blank=True, verbose_name="Banner Link 3")
    BImage4 = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="Banner Image 4")
    Blink4 = models.URLField(max_length=100, null=True, blank=True, verbose_name="Banner Link 4")
    BImage5 = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="Banner Image 5")
    Blink5 = models.URLField(max_length=100, null=True, blank=True, verbose_name="Banner Link 5")


    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
