from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

#Create a hello world view
# Create your views here.
def TestView(request, **kwargs):
    return HttpResponse("Hello world");
