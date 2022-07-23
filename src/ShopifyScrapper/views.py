import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import requests
import bs4
from .models import *
from .helper import Product

def getData(request):
    urls = Url.objects.filter(website__status=True)

    for url in urls:

        # TODO: Logic to break the data into pages
        store_url = url.url + "/products.json?limit=1"
        req = requests.get(store_url)
        data = req.json()
        for product in data["products"]:
            do_exist = Data.objects.filter(product_id=product["id"]).exists()
            if do_exist == False:
                product_obj = Product(product, url.website)
                product_obj.Data()
                product_obj.Variants()
                product_obj.ProductImages()
    return HttpResponse(urls)