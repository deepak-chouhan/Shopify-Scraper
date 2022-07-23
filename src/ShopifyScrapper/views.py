import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import requests
import bs4
from .models import *

def getData(request):
    urls = Url.objects.filter(website__status=True)
    # req = requests.get(urls[0].url)
    # data = req.json()
    for url in urls:
        print(f"{url.website}: {url.url}")
        
    return HttpResponse(urls)