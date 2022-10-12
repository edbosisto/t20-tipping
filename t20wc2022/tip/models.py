
from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=200)
    matches_won = models.PositiveIntegerField()
    eliminated = models.BooleanField(default=False)

    def __str__(self):
        return self.id + self.name


class Venue(models.Model):
    stadium = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.id + self.stadium


class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team1")
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team2")
    local_time = models.TimeField()
    your_time = models.TimeField()
    date = models.DateField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, default=None, on_delete=models.CASCADE, related_name="winner")

    def __str__(self):
        return self.id + ": " + self.team1 + " VS " + self.team2
