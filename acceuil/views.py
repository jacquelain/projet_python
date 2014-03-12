# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse,Http404

def admin (request):
    return render(admin)