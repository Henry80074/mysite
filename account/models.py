from django.db import models
from django.contrib.auth.models import User
from main.models import TherapyActivity
import recurrence
from recurrence.fields import RecurrenceField

Fav_CHOICES = (
    ('Favourite', 'Favourite'),
    ('Unfavourite', 'Unfavourite'),
)


class UserFavourite(models.Model):
    therapy_activity = models.ForeignKey(TherapyActivity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    value = models.CharField(choices=Fav_CHOICES, max_length=11)

    def __str__(self):
        return f"{self.user}-{self.value}"


class UserTherapyActivity(models.Model):
    therapy_activity = models.ForeignKey(TherapyActivity, on_delete=models.CASCADE)
    reps = models.IntegerField("reps", default=None, null=True, blank=True)
    sets = models.IntegerField("reps", default=None, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class TherapyProgramme(models.Model):
    therapy_list = models.ManyToManyField(UserTherapyActivity)
    recurrences = recurrence.fields.RecurrenceField()
