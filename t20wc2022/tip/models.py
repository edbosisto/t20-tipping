from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=200)
    ranking = models.PositiveIntegerField(default=None)
    matches_won = models.PositiveIntegerField(default=0)
    eliminated = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Venue(models.Model):
    stadium = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.stadium


class Match(models.Model):
    team1 = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE, related_name="team1")
    team2 = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE, related_name="team2")
    when = models.DateTimeField(blank=True, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE, related_name="winner")

    # def __str__(self):
    #     return f"{self.id}: {self.team1} vs {self.team2} in {self.venue} at {self.when}"


class Tip(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="match")
    tip = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="tip")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
