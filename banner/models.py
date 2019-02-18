from django.db import models

# Create your models here.
class banner(models.Model):
    bimage1 = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="Banner Image 1")
    blink1 = models.URLField(max_length=100, null=True, blank=True, verbose_name="Banner Link 1")
    bimage2 = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="Banner Image 2")
    blink2 = models.URLField(max_length=100, null=True, blank=True, verbose_name="Banner Link 2")
    bimage3 = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="Banner Image 3")
    blink3 = models.URLField(max_length=100, null=True, blank=True, verbose_name="Banner Link 3")
    bimage4 = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="Banner Image 4")
    blink4 = models.URLField(max_length=100, null=True, blank=True, verbose_name="Banner Link 4")
    bimage5 = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="Banner Image 5")
    blink5 = models.URLField(max_length=100, null=True, blank=True, verbose_name="Banner Link 5")
    hanin = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="Hanin")
    program = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="Program")
    leasedeal = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="leasedeal")
    rental = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="rental")
    migration = models.ImageField(null=True, blank=False, upload_to="banner", verbose_name="migration")

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"


