from django.shortcuts import render, redirect
from django.http import HttpResponse

import uuid
from .models import Url
# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    if(request.method == 'POST'):
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link = url, uuid = uid)
        new_url.save()

        return HttpResponse(uid)

def go(request, pk):
    urls_details = Url.objects.get(uuid = pk)

    return redirect(urls_details.link)
