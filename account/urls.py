from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path("favourite_list/", views.favourite_list, name="favourite_list"),
    path("favourite_unfavourite/", views.favourite_unfavourite, name="favourite_unfavourite"),
    path("favourite_add/<int:id>/", views.favourite_add, name="favourite_add"),
    path("create_user_therapy_activity/", views.create_user_therapy_activity, name="create-programme"),
    path("create_therapy_programme/", views.create_programme, name="create_therapy_programme"),
    path("update_therapy_activities/<int:id>", views.update_user_therapy_activity, name="update_therapy_activities"),
    path("delete_user_therapy_activity/<int:id>/", views.delete_user_therapy_activity, name="delete_user_therapy_activity"),
    path("CreateProgramme/", views.CreateTherapyProgramme, name="CreateProgramme")
    ]