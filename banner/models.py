from django.db import models

# Create your models here.
class banner(models.Model):
    BImage1 = models.ImageField(null=True, blank=True, upload_to="banner")
    BImage2 = models.ImageField(null=True, blank=True, upload_to="banner")
    BImage3 = models.ImageField(null=True, blank=True, upload_to="banner")
    BImage4 = models.ImageField(null=True, blank=True, upload_to="banner")
    BImage5 = models.ImageField(null=True, blank=True, upload_to="banner")
    BImage6 = models.ImageField(null=True, blank=True, upload_to="banner")
    BImage7 = models.ImageField(null=True, blank=True, upload_to="banner")
    BImage8 = models.ImageField(null=True, blank=True, upload_to="banner")
    BImage9 = models.ImageField(null=True, blank=True, upload_to="banner")
    BImage10 = models.ImageField(null=True, blank=True, upload_to="banner")
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
