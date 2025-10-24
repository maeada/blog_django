# https://docs.djangoproject.com/en/5.2/topics/http/urls/
from django.urls import path
from . import views

# add namespace to our URLconf.
app_name = 'blogs'

urlpatterns = [
    path('testing', views.index, name='index'),
    path('', views.home, name='home')
]