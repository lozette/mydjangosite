from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'mydjangosite/index.html')
