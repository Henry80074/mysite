from django.contrib.auth import login, authenticate
from django.forms import ModelForm
from django import forms
from .models import UserTherapyActivity, TherapyProgramme  #therapy_programme contains the recurrence fields
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
        fields = ['reps', 'sets']


class TherapyProgrammeForm(ModelForm):

    #def __init__(self, *args, **kwargs):
        #""" Grants access to the request object so that only activities of the current user
        #are given as options"""

        #self.request = kwargs.pop('request')
        #super(TherapyProgrammeForm, self).__init__(*args, **kwargs)
        #self.fields['therapy_list'].queryset = UserTherapyActivity.objects.filter(
            #user=self.request.user)

    class Meta:
        model = TherapyProgramme
        fields = ['therapy_list', 'user']

    #therapy_list = forms.ModelMultipleChoiceField(queryset=None)
    #recurrences =


#class TherapyProgramme(forms.Form):
 #   activities = forms.(label='Your name', max_length=100)
  #  reps = forms.IntegerField(label="reps", max_length=3)
   # sets = forms.IntegerField(label="sets", max_length=3)