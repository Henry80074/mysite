from django import forms
from django.forms import ModelForm
from main.models import TherapyActivity

class TherapyProgramme(forms.Form):
    activities = forms.(label='Your name', max_length=100)
    reps = forms.IntegerField(label="reps", max_length=3)
    sets = forms.IntegerField(label="sets", max_length=3)

class TherapyProgrammeForm(ModelForm):
    class Meta:
        model  =  TherapyActivity
    activities = forms.(label='Your name', max_length=100)
    reps = forms.IntegerField(label="reps", max_length=3)
    sets = forms.IntegerField(label="sets", max_length=3)
