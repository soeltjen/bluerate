from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader

from .models import Officer

# Create your views here.

def index(request):
    return HttpResponse("This is the review page.")

def profile(request, officer_id):
    officer_data = Officers.objects.raw('SELECT * FROM officers \
                                       WHERE profileid==officer_id')
    context = {'officer_data': officer_data}
    return render(request,'profile.html',context)

def add_review(request):
    return HttpResponse()

def search(request):
    template = loader.get_template('results.html')
    context = {
            'officers' : None
    }
    return HttpResponse(template.render(context, request))
