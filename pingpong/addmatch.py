import os
import django
import operator
from datetime import date

def update_rank():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pingpong.settings')
    django.setup()
    from points.models import Player, Match, MatchArchive
    play = Player.objects.order_by('-points')
    current = 1
    for h in play:
        h.rank = current
        current += 1
    

def new_player(name, email, rank=10000, points=0):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pingpong.settings')
    django.setup()
    from points.models import Player, Match, MatchArchive
    p = Player(name = name, email = email, rank = rank, points= points)
    p.save()

def new_match(loser, winner, timestamp):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pingpong.settings')
    django.setup()
    from points.models import Player, Match, MatchArchive
    match = Match(loser=loser, winner=winner, date=timestamp)
    match.save()
    return match

def update_players():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pingpong.settings')
    django.setup()
    from points.models import Player, Match, MatchArchive

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
        

if __name__ == '__main__':
    print("Starting Rango population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pingpong.settings')
    django.setup()
    from points.models import Player, Match, MatchArchive
##    new_match(loser = Player.objects.get(name="Jacob"),
##              winner = Player.objects.get(name="Trey"),
##              timestamp=date.today())
    
    update_players()
    update_rank()
