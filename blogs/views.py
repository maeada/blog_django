# https://docs.djangoproject.com/en/5.2/intro/tutorial03/
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Content

# Create your views here.
def index(request):
    # content = "Hello first my blog application with django framwork"
    latest_content_list = Content.objects.order_by("updated")[:5]
    content = ", ".join([obj.subject for obj in latest_content_list])

    return HttpResponse(content)

def home(request):
    latest_content_list = Content.objects.order_by("updated")[:5]
    template = loader.get_template("blogs/home.html")
    context = {'latest_content_list': latest_content_list}    
    return HttpResponse(template.render(context)) 