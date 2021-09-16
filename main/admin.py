from django.contrib import admin
from .models import TherapyActivity
from account.models import TherapyProgramme, UserTherapyActivity
# Register your models here.
admin.site.register(TherapyActivity)
admin.site.register(TherapyProgramme)
admin.site.register(UserTherapyActivity)