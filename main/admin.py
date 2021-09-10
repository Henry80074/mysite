from django.contrib import admin
from .models import TherapyActivity
from account.models import UserTherapyActivity, TherapyProgramme
# Register your models here.
admin.site.register(TherapyActivity)
admin.site.register(UserTherapyActivity)
admin.site.register(TherapyProgramme)
