from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Document

class IndexView(generic.ListView):
    template_name = 'documents/index.html'

    def get_queryset(self):
        return Document.objects.all()

class DetailView(generic.DetailView):
    model = Document
    template_name = 'documents/detail.html'
