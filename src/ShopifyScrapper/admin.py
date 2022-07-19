from django.contrib import admin
from .models import *

class UrlAdmin(admin.ModelAdmin):
    list_display = ("website", "url",)

class WebsiteInline(admin.TabularInline):
    model = Url

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ("name", "status",)
    inlines = [WebsiteInline]

class DataAdmin(admin.ModelAdmin):
    list_display = ("website", "retailer", "product_type", "price", "stock_code",)


admin.site.register(Url, UrlAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Data, DataAdmin)
