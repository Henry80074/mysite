from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path("favourite_list/", views.favourite_list, name="favourite_list"),
    path("favourite_unfavourite/", views.favourite_unfavourite, name="favourite_unfavourite"),
    path("favourite_add/<int:id>/", views.favourite_add, name="favourite_add"),
    path("create_programme/", views.create_programme, name="create-programme"),
    ]