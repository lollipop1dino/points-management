from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='standings'),
    path('matchsubmission', views.matchsubmission, name='matchsubmission')
]

