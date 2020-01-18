from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField()
    rank = models.IntegerField()
    points = models.IntegerField()
    
    def __unicode__(self):
        return self.name

class Matches(models.Model):
    players = models.ManyToManyField(Player, related_name='player_playing')
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_won')

    date = models.DateField()
    
    def __unicode__(self):
        return self.date


