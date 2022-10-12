from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('account/', views.account, name="account"),
    path('ladder/', views.ladder, name="ladder"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('matches/', views.matches, name="matches"),
    path('teams/', views.teams, name="teams"),
    path('tip/', views.tip, name="tip"),
]
