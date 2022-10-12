from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Team, Venue, Match
from .serializers import TeamSerializer, VenueSerializer, MatchSerializer

# Create your views here.

MATCHES = Match.objects.all()
VENUES = Venue.objects.all()
TEAMS = Team.objects.all()


### HOMEPAGE ###

def home(request):
    matches = MatchSerializer(MATCHES, many=True).data

    context = {"matches": matches}
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
    return render(request, "teams", context)


def tip(request):
    return render(request, "tip.html", {})
