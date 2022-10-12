from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


### HOMEPAGE ###

def home(request):
    return render(request, "home.html", {})


def account(request):
    return render(request, "login.html", {})


def loginPage(request):
    return render(request, "login.html", {})


def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('home')


def registerPage(request):
    return render(request, "register.html", {})


def schedule(request):
    return render(request, "schedule.html", {})


def teams(request):
    return render(request, "teams", {})


def tip(request):
    return render(request, "tip.html", {})
