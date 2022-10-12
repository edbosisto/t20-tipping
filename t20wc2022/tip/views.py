from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

import datetime
from .models import Team, Venue, Match
from .serializers import TeamSerializer, VenueSerializer, MatchSerializer
from .forms import TipForm

# Create your views here.

MATCHES = Match.objects.all()
VENUES = Venue.objects.all()
TEAMS = Team.objects.all()

NOW = datetime.datetime.now()

### HOMEPAGE ###

def home(request):
    matches = MatchSerializer(MATCHES, many=True).data

    # Get current date and time
    now = NOW.strftime("%Y-%m-%d")

    # Get list of matches id with today's date
    match_ids_today = []
    for match in range(len(matches)):
        if now == matches[match]["when"].split("T")[0]:
            match_ids_today.append(match + 1)
    print(match_ids_today)
    
    # Get queryset of matches with today's date using match id list
    matches_today = []
    for id in match_ids_today:
        match = MATCHES.get(id=id)

    ############### COME BACK TO THIS ####################

    next = matches[0]
    team1 = TEAMS.get(id=next["team1"])
    team2 = TEAMS.get(id=next["team2"])
    datetime = next["when"]
    date = datetime.split("T")[0]
    time = datetime.split("T")[1]
    venue = VENUES.get(id=next["venue"])

    context = {
        "matches": matches,
        "now": now,
        "next": next,
        "team1": team1,
        "team2": team2,
        "date": date,
        "time": time,
        "venue": venue,
    }
    return render(request, "home.html", context)


def account(request):
    return render(request, "login.html", {})


def ladder(request):
    return render(request, "ladder.html", {})


def loginPage(request):
    return render(request, "login.html", {})


def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('home')


def registerPage(request):
    return render(request, "register.html", {})


def matches(request):
    matches = MatchSerializer(MATCHES, many=True).data

    context = {"matches": matches}
    return render(request, "matches.html", context)


def teams(request):
    teams = TeamSerializer(TEAMS, many=True)

    context = {"teams": teams}
    return render(request, "teams.html", context)


def tips(request):
    return render(request, "tips.html", {})
