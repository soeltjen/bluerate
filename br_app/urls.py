from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('profile/<int:officer_id>/',views.profile, name='profile'),
    path('add', views.add_review, name='add_review'),
    path('search', views.search, name='search'),
]
