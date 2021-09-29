from .forms import RegisterForm, UserTherapyActivityForm, TherapyProgrammeForm
from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from main.models import TherapyActivity
from account.models import UserTherapyActivity, TherapyProgramme
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView


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
        favourite, created = UserTherapyActivity.objects.get_or_create(user=user,
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


def update_user_therapy_activity(request):

    if request.method == 'POST':
        form = UserTherapyActivityForm(request.POST)
        if form.is_valid():
            user = request.user
            activity_id_list = request.POST.getlist('checkbox')
            for activity_id in activity_id_list:
                activity = get_object_or_404(TherapyActivity, id=activity_id)
                sets = request.POST[activity_id + 'sets']
                reps = request.POST[activity_id + 'reps']
                UserTherapyActivity.objects.update(sets=sets, reps=reps, therapy_activity=activity, user=user, value="Favourite")
        else:
            print(form.errors)

    return redirect('/account/create_therapy_programme/')


def create_user_therapy_activity(request):

    if request.method == 'POST':
        print("post")
        form = UserTherapyActivityForm(request.POST)
        if form.is_valid():
            user = request.user
            activity_id_list = request.POST.getlist('checkbox')
            for activity_id in activity_id_list:
                activity = get_object_or_404(TherapyActivity, id=activity_id)
                sets = request.POST[activity_id + 'sets']
                reps = request.POST[activity_id + 'reps']
                print("creating")
                UserTherapyActivity.objects.create(sets=sets, reps=reps, therapy_activity=activity, user=user, value="Favourite")
        else:
            print(form.errors)

    return redirect('/account/create_therapy_programme/')


def delete_user_therapy_activity(request, id):

    user_therapy_activity = get_object_or_404(UserTherapyActivity, id=id)
    user_therapy_activity.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def create_programme(request):
    UserTherapyActivities = UserTherapyActivity.objects.filter(user=request.user)
    context = {'UserTherapyActivities': UserTherapyActivities}

    return render(request, 'account/create_programme.html', context)


def CreateTherapyProgramme(request): # consider reworking the models to make TherapyActivity/ UserTherapyActivity Obsolete?

    if request.method == 'POST' and 'update-all' in request.POST:
        form = UserTherapyActivityForm(request.POST) #work with checkboxes to make them useful when creating programme.
        if form.is_valid():
            activity_id_list = []
            activity_id_list = request.POST.getlist('checkbox')
            for activity_id in activity_id_list: #this is inefficient code that requires multiple database queries, consider bulk_update
                sets = request.POST[activity_id + 'sets']
                reps = request.POST[activity_id + 'reps']
                UserTherapyActivity.objects.select_for_update().filter(id=activity_id).update(sets=sets, reps=reps)

        else:
            print(form.errors)

    if request.method == 'POST' and 'update-this' in request.POST:
        form = UserTherapyActivityForm(request.POST) #work with checkboxes to make them useful when creating programme.
        if form.is_valid():
            activity_id = request.POST.get("update-this")
            print(activity_id)
            sets = request.POST[activity_id + 'sets']
            reps = request.POST[activity_id + 'reps']
            UserTherapyActivity.objects.select_for_update().filter(id=activity_id).update(sets=sets, reps=reps)

        else:
            print(form.errors)

    if request.method == 'POST' and 'create-programme' in request.POST:
        form = TherapyProgrammeForm(request.POST)
        if form.is_valid():
            user = request.user
            activity_id_list = request.POST.getlist('checkbox')
            instance = TherapyProgramme.objects.create(user=user)
            for activity_id in activity_id_list:
                activity = get_object_or_404(UserTherapyActivity, id=activity_id)
                instance.therapy_list.add(activity)

        else:
            print(form.errors)

    return redirect('/account/create_therapy_programme/')



#    def get_form_kwargs(self):
#        """ Passes the request object to the form class.
#         This is necessary to only display members that belong to a given user"""
#
#        kwargs = super(CreateTherapyProgramme, self).get_form_kwargs()
#        kwargs['request'] = self.request
#        return kwargs
#
#    return redirect('/account/create_therapy_programme/')





