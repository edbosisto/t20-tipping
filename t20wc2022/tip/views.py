from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

import datetime
from .models import Team, Tip, Venue, Match
from .serializers import TeamSerializer, VenueSerializer, MatchSerializer
from .forms import TipForm

# Create your views here.

MATCHES = Match.objects.all()
VENUES = Venue.objects.all()
TEAMS = Team.objects.all()
TIPS = Tip.objects.all()


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


@login_required(login_url='login')
def account(request):
    return render(request, "account.html", {})


@login_required(login_url='login')
def ladder(request):

    


    return render(request, "ladder.html", {})


def loginPage(request):
    # Redirect users who are already logged in away from login page.
    if request.user.is_authenticated:
        messages.error(request, "Already logged in...")
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Check if user exists
        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exist")

        # Save and check username and password
        user = authenticate(request, username=username, password=password)
        # Check if user exists, then login and redirect to homepage
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")

            # If user was redirected to login, return them to the page they were on
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            # Otherwise redirect to homepage
            else:
                return redirect('home')
        else:
            messages.error(request, "Login details incorrect")

    return render(request, 'login.html', {})


def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('home')
        else:
            messages.error(request, "An error has occured, try registration again")

    context = {
        "form": form,
    }
    return render(request, 'register.html', context)


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


@login_required(login_url='login')
def tips(request):
    form = TipForm()

    # Check user is logged in
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to submit tips")
        return redirect('login')

    # User submits a tip
    if request.method == "POST":

        # Get tip data
        user = request.user
        match_post = request.POST.get("match")
        match = MATCHES.get(id=match_post)
        tip = request.POST.get("tip")
        team = TEAMS.get(id=tip)

        # Save tip to database
        Tip.objects.create(user_id=user, match=match, tip=team)

    context = {
        "form": form,
        "matches": MATCHES,
    }
    return render(request, "tips.html", context)
