from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Officer, Review, User

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def profile(request, officer_id):
    template = loader.get_template('profile.html')
    officer = Officer.objects.raw('SELECT * FROM officer \
                                  WHERE profile_id = %s;' % (officer_id))[0]
    reviews = [p for p in Review.objects.raw('SELECT * FROM review \
                            WHERE officer_id = %s;' % (officer_id))]
    context = {'officer': officer, 'reviews': reviews, 'logged_in': True}
    return HttpResponse(template.render(context, request))

def add_review(request):
    template = loader.get_template('profile.html')
    if('submit-btn' in request.GET):
        username = request.GET.get('user')
        rating = request.GET.get('rating')
        review_text = request.GET.get('review')
        usr = User.objects.raw('SELECT * FROM user WHERE username = \'%s\';' % username)[0]
        review = Review(user=usr, description=review_text, stars=rating, officer_id=5)
        review.save()
        context = {'user':usr, 'reviews':review}
        return HttpResponse(template.render(context,request))

def search(request):
    first = request.GET.get('first')
    last = request.GET.get('last')
    badge = request.GET.get('badge')
    city = request.GET.get('city')

    first = (first if (first != '') else '%%')
    last = (last if (last != '') else '%%')
    badge = (badge if (badge != '') else '%%')
    city = (city if (city != '') else '%%')

    template = loader.get_template('results.html')
    query = 'SELECT * FROM officer WHERE firstName LIKE \'%s\' \
        AND lastName LIKE \'%s\' AND badgeNumber LIKE \'%s\' \
        AND city LIKE \'%s\';' % (first, last, badge, city)
    officers = [p for p in Officer.objects.raw(query)]
    context = {
            'officers' : officers
    }
    return HttpResponse(template.render(context, request))
