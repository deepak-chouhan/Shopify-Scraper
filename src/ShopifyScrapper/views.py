from tkinter import Scale
from django.http import HttpResponse
from .models import *
from .helper import Scrape

def getData(request):
    urls = Url.objects.filter(website__status=True)
    Scrape(urls)
    return HttpResponse(urls)