from django import forms

class WineForm(forms.Form):
    name = forms.CharField(max_length=50)
    brand = forms.CharField(max_length=50)
    price = forms.FloatField()
    aged = forms.IntegerField()
    winery = forms.CharField(max_length=50)