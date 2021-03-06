from django.contrib import admin
from .models import Car, CarImg, faqath

#1.
# class EntryAdmin(admin.StackedInline):
#     list_display = ("title", "type","created", "sold","publish")
#     prepopulated_fields = {"slug": ("title","type")}
#     model=CarImg
#
# class CarImgInLine(admin.StackedInline):
#     model = CarImg
#     extra = 3
#     inlines=[EntryAdmin]
#2.

# class CarImgInLine(admin.StackedInline):
#     model=CarImg
#     extra = 3
#
# class EntryAdmin(admin.ModelAdmin):
#     list_display = ("title", "type","created", "sold","publish")
#     prepopulated_fields = {"slug": ("title","type")}
#     inlines=[CarImgInLine]


#3.

class CarImgLine(admin.StackedInline):
    model=CarImg
    extra=1

class CarAth(admin.StackedInline):
    model=faqath
    extra = 1

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "type","created", "sold","publish")
    prepopulated_fields = {"slug": ("title","type")}
    inlines=[CarImgLine, CarAth]
    list_filter = ['type', 'sold', 'publish']




admin.site.register(Car, EntryAdmin)
# admin.site.register(CarImg, EntryAdmin)