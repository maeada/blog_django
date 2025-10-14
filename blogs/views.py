from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    content = "Hello first my blog application with django framwork"
    return HttpResponse(content)

# comment