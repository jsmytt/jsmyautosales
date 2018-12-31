from django.contrib import admin
from .models import Car

class EntryAdmin(admin.ModelAdmin):

    list_display = ("title", "type","created", "sold","publish")
    prepopulated_fields = {"slug": ("title","type")}

    '''fieldsets = [

        (None, {'fields': ['price']}),
        (None, {'fields': ['type']}),
        ('Date information2', {'fields': ['sold']}),
        ('Date information', {'fields': ['publish']}),


    ]'''
    list_filter = ['type']
admin.site.register(Car, EntryAdmin)
