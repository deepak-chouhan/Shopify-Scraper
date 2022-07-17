from django.shortcuts import render
from django.http import HttpResponse
import requests
import bs4

from .models import *

def getData(request):

    return HttpResponse("Working")
