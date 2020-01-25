from django import forms
from .models import Player

class MatchForm(forms.Form):
    p1 = forms.ModelChoiceField(queryset=Player.objects.all(), help_text="Winner Email")
    p2 = forms.ModelChoiceField(queryset=Player.objects.all(), help_text="Loser Email")

    class Meta:
        fields = ["p1","p2"]