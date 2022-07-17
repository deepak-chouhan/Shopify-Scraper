from django.contrib import admin

from .models import *

class SizeAdmin(admin.ModelAdmin):
    ordering = ("size", )

class StoreTypeAdmin(admin.ModelAdmin):
    list_display = ("web_type",)

class UrlAdmin(admin.ModelAdmin):
    list_display = ("website", "url",)

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ("name", "web_type", "status")

class DataAdmin(admin.ModelAdmin):
    list_display = ("website", "retailer", "product_type", "price", "stock_code",)


admin.site.register(Url, UrlAdmin)
admin.site.register(StoreType, StoreTypeAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Size, SizeAdmin)
