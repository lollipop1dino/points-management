import addmatch
import os
import django

if __name__ == '__main__':
    print("Starting Rango population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pingpong.settings')
    
    django.setup()
    from points.models import Player, Match 

    addmatch.new_match(Player.get
    addmatch.update_players()
