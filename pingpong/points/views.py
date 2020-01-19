from django.shortcuts import render
from django.http import HttpResponse
from .models import Player

from forms import MatchForm

def index(request):
    return render(request, 'points/index.html')

def matchsubmission(request):
    blankform = MatchForm()
    return render(request, 'points/matchsubmission.html', {'form': blankform})

def sendinmatchsubmission(request):
    form = MatchForm(request.POST)
    blank = MatchForm()
    return render(request, 'points/matchsubmission.html', {'form': blank})


def standings(request):
    ranks = Player.objects.all().order_by('rank')
    return render(request, 'points/standings.html', {'ranks': ranks)

def upcoming(request):
    return render(request, 'points/upcoming.html')

def pics(request):
    return render(request, 'points/pics.html')
