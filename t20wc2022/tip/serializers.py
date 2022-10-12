from rest_framework.serializers import ModelSerializer

from .models import Team, Venue, Match


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class VenueSerializer(ModelSerializer):
    class Meta:
        model = Venue
        fields = "__all__"


class MatchSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"
        