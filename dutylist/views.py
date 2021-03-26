from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Duty
from django.conf import settings
import os


def index(request):
    duty = Duty.objects.all().order_by('-created')
    url = settings.MEDIA_URL
    l = []
    for f in duty:
        l.append(os.path.splitext(f.__str__())[0])
    
    d = zip(duty, l)
    return render(request, 'index.html', {
         'url':url, 'duties':d })
