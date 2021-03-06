from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import TherapyActivity

# Create your views here.


def index(response):
    return render(response, 'main/home.html')


def view_all(request):

    activities = TherapyActivity.objects.all()
    user = request.user

    context = {
        'activities': activities,
        'user': user
    }
    return render(request, 'main/view_all.html', context)


def activity_single(request, activity):

    activity = get_object_or_404(TherapyActivity, slug=activity)

    fav = bool

    if activity.favourites.filter(id=request.user.id).exists():
        fav = True
    else:
        fav = False

    return render(request, 'main/therapy_activity.html', {'activity': activity, 'fav': fav})