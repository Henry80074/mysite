from django.contrib.auth import login, authenticate
from django.forms import ModelForm
from django import forms
from .models import UserTherapyActivity, TherapyProgramme #therpay_programme contaisn the recurrence fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import TherapyActivity
from datetime import datetime


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class UserTherapyActivityForm(ModelForm):
    class Meta:
        model = UserTherapyActivity
        fields = ('therapy_activity', 'reps', 'sets')


class TherapyProgrammeForm(ModelForm):
    class Meta:
        model = TherapyProgramme
        fields = ['therapy_list', 'recurrences']

#class TherapyProgramme(forms.Form):
 #   activities = forms.(label='Your name', max_length=100)
  #  reps = forms.IntegerField(label="reps", max_length=3)
   # sets = forms.IntegerField(label="sets", max_length=3)