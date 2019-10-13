from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Officer

# Create your views here.

def index(request):
    return HttpResponse("This is the review page.")

def profile(request, officer_id):
    officer_data = Officer.from_db()
    context = {'officer_data': officer_data}
    return render(request)

def add_review(request):
    return HttpResponse()

def search(request):
    first = request.GET.get('first', '%%')
    last = request.GET.get('last', '%%')
    badge = request.GET.get('badge', '%%')
    city = request.GET.get('city', '%%')
    template = loader.get_template('results.html')
    query = 'SELECT * FROM officer WHERE firstName LIKE \'%s\' AND lastName LIKE \'%s\' AND badgeNumber LIKE \'%s\' AND city LIKE \'%s\';' % (first, last, badge, city)
    print(query)
    officers = [p for p in Officer.objects.raw(query)]
    print(officers)
    context = {
            'officers' : officers
    }
    return HttpResponse(template.render(context, request))
