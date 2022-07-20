from json import JSONEncoder
import json
from django.forms import JSONField
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import bs4
from .models import *

def getData(request):
    urls = Url.objects.filter(website__status=True)
    print(urls)
    return HttpResponse(urls)
