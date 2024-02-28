from django import forms
from django.core.exceptions import ValidationError

class formExpenses(forms.Form):
    title = forms.CharField()
    cost = forms.IntegerField()
    category = forms.CharField()