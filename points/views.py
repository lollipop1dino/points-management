from django.shortcuts import render
from django.http import HttpResponse
from .models import Player
from .models import Match
import datetime
from .forms import MatchForm
from .calculation import new_match, update_players, update_rank


def index(request):
    #allusers = models.Users.objects.all()
    #for user in allusers:
    #   addmatch.new_player(name=user.name,email=user.email)
    return render(request, 'points/index.html')

def matchsubmission(request):
    blankform = MatchForm(initial = {'p1': request.user})
    print(request.user)
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            new_match(winner=form.cleaned_data['p1'], loser=form.cleaned_data['p2'], timestamp=datetime.date.today())
            update_players()
            update_rank()
        return render(request, 'points/matchsubmission.html', {'form': blankform, 'success': "Match submitted successfully"})
    return render(request, 'points/matchsubmission.html', {'form': blankform})



def standings(request):
    ranks = Player.objects.all().order_by('rank')
    return render(request, 'points/standings.html', {'ranks': ranks})

def upcoming(request):
    return render(request, 'points/upcoming.html')

def pics(request):
    return render(request, 'points/pics.html')
