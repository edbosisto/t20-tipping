from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('account/', views.account, name="account"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('schedule/', views.schedule, name="schedule"),
    path('teams/', views.teams, name="teams"),
    path('tip/', views.tip, name="tip"),
]
