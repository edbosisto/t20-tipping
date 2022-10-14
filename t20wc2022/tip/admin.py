from django.contrib import admin
from .models import Score, Team, Venue, Match, Tip

# Register your models here.

admin.site.register(Team)
admin.site.register(Venue)
admin.site.register(Match)
admin.site.register(Tip)
admin.site.register(Score)
