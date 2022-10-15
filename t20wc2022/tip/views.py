from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

import datetime
from .models import Score, Team, Tip, Venue, Match

# Create your views here.


# Tally scores for database
def tally():
    # iterate through users
    users = User.objects.all()
    for user in users:
        # find all tips by that user and current user score
        tips = Tip.objects.filter(user_id=user)
        # Set score to 0
        score = 0
        
        # iterate through tips.
        for i in tips:
            # Get match and tip values
            match = i.match
            tip = i.tip

            # Check if tip is correct
            if tip == match.winner:
                score += 1

        # Check current user score in database
        user_score = Score.objects.get(user=user).score

        # if user_score hasn't changed, don't update database
        if user_score != score:
            # Update score in database
            obj = Score.objects.get(user=user)
            obj.score = score
            obj.save()

### HOMEPAGE ###

def home(request):
    # Get today's date and tomorrow's date
    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)

    # Get queryset of matches with today's date
    match_today = Match.objects.filter(when__date=today)

    # Get next match (if no match today)
    match_next = Match.objects.filter(when__gt=tomorrow, when__year="2022")[0]

    context = {
        "match_today": match_today,
        "match_next": match_next,
    }
    return render(request, "home.html", context)


@login_required(login_url='login')
def account(request):
    # Get all tips for user and all matches
    user = request.user
    tips = Tip.objects.filter(user_id=user)
    matches = Match.objects.all()

    context = {
        "tips": tips,
        "matches": matches,
    }
    return render(request, "account.html", context)


@login_required(login_url='login')
def ladder(request):
    # Tally user scors
    tally()

    # Get current scores
    scores = Score.objects.all()

    context = {
        "scores": scores,
    }
    return render(request, "ladder.html", context)


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
            user.save()
            login(request, user)

            # Create database entry for Scores = 0 for new user
            Score.objects.create(user=user, score=0)

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
    matches_october = Match.objects.filter(when__month="10")

    # Get matches in November, not finals
    matches_november = Match.objects.filter(when__range=["2022-11-01", "2022-11-07"])

    # Get finals only
    finals = Match.objects.filter(when__range=["2022-11-08", "2022-11-14"])

    context = {
        "matches_october": matches_october,
        "matches_november": matches_november,
        "finals": finals,
    }
    return render(request, "matches.html", context)


@login_required(login_url='login')
def tips(request):
    # get matches which haven't been played yet
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    matches = Match.objects.filter(when__gt=now)

    # Check user is logged in
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to submit tips")
        return redirect('login')

    # Get existing tips for user
    user = request.user
    tips = Tip.objects.filter(user_id=user)

    # User submits a tip
    if request.method == "POST":

        # Get tip data
        user = request.user
        match_post = request.POST.get("match")
        match = Match.objects.get(id=match_post)
        tip = request.POST.get("tip")
        if not tip:
            messages.error(request, "Don't click save for matches you haven't tipped")

        team = Team.objects.get(id=tip)

        # Check if match has already occured (in case user left browser open)
        tip_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not Match.objects.filter(id=match_post, when__gt=tip_time):
            messages.error(request, "That match has already started")
            return redirect('tips')

        # Check if tip already entered. If it doesn't exist, create tip in database.
        if not Tip.objects.filter(user_id=user, match=match):
            Tip.objects.create(user_id=user, match=match, tip=team)
        else:
            # If tip exists, update
            obj = Tip.objects.get(user_id=user, match=match)
            obj.tip = team
            obj.save()
    
    # Retrieve all updated tips by the user
    tips = Tip.objects.filter(user_id=user)
    print(tips)

    context = {
        "matches": matches,
        "tips": tips,
    }
    return render(request, "tips.html", context)
