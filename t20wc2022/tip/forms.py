from django.forms import ModelForm
from .models import Tip


# form not needed
class TipForm(ModelForm):
    class Meta:
        model = Tip
        fields = ["match", "tip"]
