from django.db import models
from ckeditor.fields import RichTextField

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Car(models.Model):
    type = models.CharField(max_length=25, choices=[('New', 'New Vehicle'), ('Used', 'Used Vehicle'), ('Lease', 'Lease Vehicle')], default='New', verbose_name='Listing Type')
    title = models.CharField(max_length=200, verbose_name='Title of Vehicle Listing')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Price of Vehicle in Dollar Amount')
    body = RichTextField(verbose_name='Description of Vehicle')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='SLUG: Your URL will have this in the address')
    publish = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    object = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Car Listing Entry"
        verbose_name_plural = "Car Listing Entries"
        ordering = ["-created"]



# ***** model for creating comment field ******
# class Comment(models.Model):
#     post = models.ForeignKey('listing.post', on_delete=models.CASCADE, related_name='comments')
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(auto_now_add=True)
#     approved_comment = models.BooleanField(default=False)
#
#     def approve(self):
#         self.approved_comment = True
#         self.save()
#
#     def __str__(self):
#         return self.text

