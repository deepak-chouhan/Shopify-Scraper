from django.contrib import admin
from .models import *

# Tabular Inline
class UrlInline(admin.TabularInline):
    model = Url

class ImageInline(admin.TabularInline):
    model = Image

class VariantInline(admin.TabularInline):
    model = Variant

# Admin
class UrlAdmin(admin.ModelAdmin):
    list_display = ("website", "url",)

class VariantAdmin(admin.ModelAdmin):
    list_display = ("title", "price")

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ("name", "status",)
    inlines = [UrlInline]

class DataAdmin(admin.ModelAdmin):
    list_display = ("website", "title", "retailer", "product_type",)
    inlines = [ImageInline, VariantInline]


admin.site.register(Url, UrlAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Variant, VariantAdmin)
