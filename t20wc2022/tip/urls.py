from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('', views.account, name="account"),
    path('', views.loginPage, name="login"),
    path('', views.registerPage, name="register"),
    path('', views.schedule, name="schedule"),
    path('', views.teams, name="teams"),
    path('', views.tip, name="tip"),
]
