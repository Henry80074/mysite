
from django.contrib import admin
from django.urls import path, include
from account import views as v
from main import views
#from create_programme import views as v2

urlpatterns = [
    path("", views.index, name="index"),
    path('main/', include('main.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path('logout_page/', v.logged_out, name='logout'),
    path('', include("django.contrib.auth.urls")),
    ]
