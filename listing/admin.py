from django.contrib import admin
from . import models

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "type","created", "sold","publish")
    prepopulated_fields = {"slug": ("title","type")}

admin.site.register(models.Car, EntryAdmin)
