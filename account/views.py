from .forms import RegisterForm, UserTherapyActivityForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from main.models import TherapyActivity
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


def create_programme(response):
    form = UserTherapyActivityForm
    return render(response, 'account/create_programme.html', {'form': form})

def logged_out(response):
    return render(response, "main/logout_page.html")

def register(response):
    if response.method =="POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            
        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "account/register.html", {"form":form})


@ login_required
def favourite_list(request):
    new = TherapyActivity.objects.filter(favourites=request.user)
    context = {'new': new}
    return render(request,
                  'account/favourites.html',
                   context)


@ login_required
def favourite_add(request, id):
    therapy_activity = get_object_or_404(TherapyActivity, id=id)
    if therapy_activity.favourites.filter(id=request.user.id).exists():
        therapy_activity.favourites.remove(request.user)
    else:
        therapy_activity.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def favourite_unfavourite(request):
    html = None
    #if request.method == 'POST':
    activity_id = request.POST.get('activity_id')
    activity = get_object_or_404(TherapyActivity, id=activity_id)
    is_fav = False
    if activity.favourites.filter(id=request.user.id).exists():
        activity.favourites.remove(request.user)
        is_fav = False
    else:
        activity.favourites.add(request.user)
        is_fav = True
    context = {
        'activity': activity,
        'is_fav': is_fav,
        'value': activity_id
        }
    if request.is_ajax():
        html = render_to_string('main/favourite_section.html', context, request=request)
    return JsonResponse({'form': html})


def logged_out(response):
    return render(response, "account/logout_page.html")