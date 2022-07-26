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
    list_display = ("variant_id", "title", "price", "sku", "product")

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ("name", "status",)
    inlines = [UrlInline]

class DataAdmin(admin.ModelAdmin):
    list_display = ("product_id", "website", "title", "retailer", "product_type",)
    inlines = [ImageInline, VariantInline]

class ImageAdmin(admin.ModelAdmin):
    list_display = ("image_url", "product")


admin.site.register(Url, UrlAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(Image, ImageAdmin)
