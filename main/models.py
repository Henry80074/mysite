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
    image = models.ImageField(null=True, blank=True, upload_to='media/')

    def get_absolute_url(self):
        return reverse('main:activity_single', args=[self.slug])

    def __str__(self):
        return self.name

