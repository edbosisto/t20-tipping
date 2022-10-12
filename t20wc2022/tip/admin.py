from django.contrib import admin
from .models import Team, Venue, Match

# Register your models here.

admin.site.register(Team)
admin.site.register(Venue)
admin.site.register(Match)
