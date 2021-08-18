from django.contrib.auth import login, authenticate
from django.forms import ModelForm
from main.models import UserTherapyActivity
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class UserTherapyActivityForm(ModelForm):
    class Meta:
        model = UserTherapyActivity
        fields = ('therapy_activity', 'reps', 'user')