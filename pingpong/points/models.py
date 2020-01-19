from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField()
    rank = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

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
