from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'points/standings.html')

def matchsubmission(request):
    return render(request, 'points/matchsubmission.html')


