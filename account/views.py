from .forms import RegisterForm, UserTherapyActivityForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from main.models import TherapyActivity
from account.models import UserFavourite, UserTherapyActivity
from django.contrib.auth.decorators import login_required


def logged_out(response):
    return render(response, "main/logout_page.html")


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            
        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "account/register.html", {"form": form})


@ login_required
def favourite_list(request):
    favourites = TherapyActivity.objects.filter(favourites=request.user)
    context = {'favourites': favourites}
    return render(request,
                  'account/favourites.html', context)


@ login_required
def favourite_add(request, id):
    therapy_activity = get_object_or_404(TherapyActivity, id=id)
    if therapy_activity.favourites.filter(id=request.user.id).exists():
        therapy_activity.favourites.remove(request.user)
    else:
        therapy_activity.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def favourite_unfavourite(request):

    user = request.user
    if request.method == 'POST':
        activity_id = request.POST.get('activity_id')
        activity = get_object_or_404(TherapyActivity, id=activity_id)

        if user in activity.favourites.all():
            activity.favourites.remove(user)
        else:
            activity.favourites.add(user)
# where is therapy_activity_id?
        favourite, created = UserFavourite.objects.get_or_create(user=user,
                                                                 therapy_activity_id=activity_id)

    if not created:
        if favourite.value == 'Favourite':
            favourite.value = 'Unfavourite'
        else:
            favourite.value = 'Favourite'
            activity.save()
            favourite.save()

        #    context = {
        #   'activity': activity,
        #   'favourite': favourite,
        #   'value': favourite.value
        #  }
    return redirect('main:view-all')


def logged_out(response):
    return render(response, "account/logout_page.html")


def create_user_therapy_activity(request):
    user = request.user
    print(user)

    if request.method == 'POST':
        form = UserTherapyActivityForm(request.POST)
        if form.is_valid():
            activity = request.POST.get('checkbox')
            print("+++" + activity)
            sets = request.POST.get("sets")
            reps = request.POST.get("reps")
            UserTherapyActivity.objects.create(sets=sets, reps=reps, therapy_activity=activity, user=request.user)
        else:
            print(form.errors)

    return render(request, 'account/favourites.html', {'form': form})
