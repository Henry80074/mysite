from django.db import models
import recurrence.fields
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class TherapyActivity(models.Model):
    name = models.CharField("Activity_Name", default=None, max_length=300)
    slug = models.SlugField(unique=True, null=True, max_length=250)
    description = models.TextField("Description", default=None)
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True
    )

    def get_absolute_url(self):
        return reverse('main:activity_single', args=[self.slug])

    def __str__(self):
        return self.name


class UserTherapySession(models.Model):
    therapy_list = models.ManyToManyField('UserTherapyActivity')
    recurrences = recurrence.fields.RecurrenceField()


class UserTherapyActivity(models.Model):
    therapy_activity = models.ForeignKey(TherapyActivity, on_delete=models.CASCADE, default=None)
    reps = models.IntegerField("reps", default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
