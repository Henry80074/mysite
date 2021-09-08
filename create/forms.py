from django import forms

class TherapyProgramme(forms.Form):
    activities = forms.CharField(label='Your name', max_length=100)