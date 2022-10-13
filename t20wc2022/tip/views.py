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
    # Get today's date and tomorrow's date
    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)

    # Get queryset of matches with today's date
    match_today = MATCHES.filter(when__date=today)

    # Get next match (if no match today)
    match_next = MATCHES.filter(when__gt=tomorrow, when__year="2022")[0]

    context = {
        "match_today": match_today,
        "match_next": match_next,
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
    # Get matches in October
    matches_october = MATCHES.filter(when__month="10")

    # Get matches in November, not finals
    matches_november = MATCHES.filter(when__range=["2022-11-01", "2022-11-07"])

    # Get finals only
    finals = MATCHES.filter(when__range=["2022-11-08", "2022-11-14"])

    context = {
        "matches_october": matches_october,
        "matches_november": matches_november,
        "finals": finals,
    }
    return render(request, "matches.html", context)


def teams(request):
    teams = TeamSerializer(TEAMS, many=True)

    context = {"teams": teams}
    return render(request, "teams.html", context)


def tips(request):
    form = TipForm()
    
    context = {
        "form": form,
        "matches": MATCHES,
    }
    return render(request, "tips.html", context)
