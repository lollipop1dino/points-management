from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('matchsubmission', views.matchsubmission, name='matchsubmission'),
    path('standings', views.standings, name='standings'),
    path('upcoming', views.upcoming, name='upcoming'),
    path('pics', views.pics, name='pics'),
]

