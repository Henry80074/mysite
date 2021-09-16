from django.db import models
from django.contrib.auth.models import User
from main.models import TherapyActivity
import recurrence
from recurrence.fields import RecurrenceField

Fav_CHOICES = (
    ('Favourite', 'Favourite'),
    ('Unfavourite', 'Unfavourite'),
)


class UserTherapyActivity(models.Model):
    therapy_activity = models.ForeignKey(TherapyActivity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    reps = models.IntegerField("reps", default=None, null=True, blank=True)
    sets = models.IntegerField("sets", default=None, null=True, blank=True)
    value = models.CharField(choices=Fav_CHOICES, max_length=11, default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.user}-{self.value}"


class TherapyProgramme(models.Model):
    therapy_list = models.ManyToManyField(UserTherapyActivity)
    #recurrences = recurrence.fields.RecurrenceField()



#    therapy_activity = models.ForeignKey(TherapyActivity, on_delete=models.CASCADE)
#    reps = models.IntegerField("reps", default=None, null=True, blank=True)
#    sets = models.IntegerField("sets", default=None, null=True, blank=True)
#    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)



