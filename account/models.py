from django.db import models
from django.contrib.auth.models import User
from main.models import TherapyActivity
from recurrence.fields import RecurrenceField

Fav_CHOICES = (
    ('Favourite', 'Favourite'),
    ('Unfavourite', 'Unfavourite'),
)


class Favourite(models.Model):
    therapy_activity = models.ForeignKey(TherapyActivity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    value = models.CharField(choices=Fav_CHOICES, max_length=11)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"


class TherapyProgramme(models.Model):
    therapy_list = models.ManyToManyField('UserTherapyActivity')
    recurrences = recurrence.fields.RecurrenceField()


class UserTherapyActivity(models.Model):
    therapy_activity = models.ForeignKey(TherapyActivity, on_delete=models.CASCADE, default=None)
    reps = models.IntegerField("reps", default=None)
    sets = models.IntegerField("reps", default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

