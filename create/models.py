from django.contrib.auth.models import User
from django.db import models
from main.models import TherapyActivity


class UserTherapySession(models.Model):
    therapy_list = models.ManyToManyField('UserTherapyActivity')
    #recurrences = recurrence.fields.RecurrenceField()


class UserTherapyActivity(models.Model):
    therapy_activity = models.ForeignKey(TherapyActivity, on_delete=models.CASCADE, default=None)
    reps = models.IntegerField("reps", default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)