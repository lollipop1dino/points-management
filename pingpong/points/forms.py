from django import forms

class MatchForm(forms.Form):
    p1 = forms.EmailField(help_text="Winner Email")
    p2 = forms.EmailField(help_text="Loser Email")
    class Meta:
        fields = ["p1","p2"]