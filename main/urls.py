
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
path("index/", views.index, name="index"),
path("view_all/", views.view_all, name="view-all"),
path("<slug:activity>/", views.activity_single, name="activity_single")
]
