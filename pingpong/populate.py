import os
import django
from datetime import date

def populate():
    player1 = add_player(name="Jacob",
        points=20,
        rank=1)

    player2 = add_player(name="Trey",
        points=19,
        rank=2)
    
    add_match(loser=player2,
              winner = player1)

##    add_page(cat=python_cat,
##        title="Learn Python in 10 Minutes",
##        url="http://www.korokithakis.net/tutorials/python/")
##
##    django_cat = add_cat("Django")
##
##    add_page(cat=django_cat,
##        title="Official Django Tutorial",
##        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
##
##    add_page(cat=django_cat,
##        title="Django Rocks",
##        url="http://www.djangorocks.com/")
##
##    add_page(cat=django_cat,
##        title="How to Tango with Django",
##        url="http://www.tangowithdjango.com/")
##
##    frame_cat = add_cat("Other Frameworks")
##
##    add_page(cat=frame_cat,
##        title="Bottle",
##        url="http://bottlepy.org/docs/dev/")
##
##    add_page(cat=frame_cat,
##        title="Flask",
##        url="http://flask.pocoo.org")

    # Print out what we have added to the user.
##    for c in Category.objects.all():
##        for p in Page.objects.filter(category=c):
##            print "- {0} - {1}".format(str(c), str(p))
##
def add_player(name, points, rank):
    p = Player.objects.get_or_create(name=name, points=points, rank=rank)[0]
    return p

def add_match(loser, winner):
    
    c = Match.objects.get_or_create(loser = loser, winner = winner, date=date.today())[0]
    
    # c.loser.add(loser)
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pingpong.settings')
    print(os.getcwd())

    
    django.setup()
    from points.models import Player, Match
    populate()
