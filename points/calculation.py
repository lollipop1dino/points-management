import os
import django
import operator
from datetime import date
from .models import Player
from .models import Match
from .models import MatchArchive

def update_rank():
    play = Player.objects.order_by('-points')
    current = 1
    for h in play:
        current += 1
        h.rank = current

def new_match(loser, winner, timestamp):
    
    match = Match(loser=loser, winner=winner, date=timestamp)
    match.save()
    return match

def update_players():
    for mat in Match.objects.all():
        print("hi")
        arch = MatchArchive(loser = mat.loser, winner = mat.winner, date = mat.date) 
        arch.save()
        if mat.loser.rank <= 5 and mat.winner.rank > 5:
            mat.winner.points += (12 - mat.loser.rank * 2)
        else:
            mat.winner.points += 1
        mat.loser.save()
        mat.winner.save()
    Match.objects.all().delete()
        
