from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Officer

# Create your views here.

def index(request):
    return HttpResponse("This is the review page.")

def profile(request, officer_id):
    officer_data = Officer.from_db()
    template = loader.get_template('officer.html')
    context = {}
    return HttpResponse("Badge number:")

def add_review(request):
    return HttpResponse()

def search(request):
    return HttpResponse()
