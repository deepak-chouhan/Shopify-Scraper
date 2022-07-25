from tkinter import Scale
from django.http import HttpResponse
from .models import *
from .helper import runScrape
import schedule
import time

schedule.every(1).minutes.do(runScrape)

def getData(request):
    while True:
        schedule.run_pending()
        time.sleep(1)