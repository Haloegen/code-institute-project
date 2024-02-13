from django import forms

class formExpenses(forms.Form):
    title = forms.CharField()
    cost = forms.IntegerField()
    category = forms.CharField()