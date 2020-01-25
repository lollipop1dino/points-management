from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Player(AbstractUser):
    rank = models.IntegerField(default=10000)
    points = models.IntegerField(default=0)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username']

    def __str__(self):
        return self.first_name + " " + self.last_name

class Match(models.Model):
    loser = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='loser')
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='winner')

    date = models.DateField()
    
    def __str__(self):
        return self.winner.name + " " + self.loser.name

class MatchArchive(models.Model):
    loser = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='loser_archive')
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='winner_archive')
    
    date = models.DateField()

    def __str__(self):
        return self.winner.name + " " + self.loser.name
