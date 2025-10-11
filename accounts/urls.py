from django.urls import path,include

from . import views

app_name = "accounts"
urlpatterns = [
    path("login/",include('django.contrib.auth.urls')),
    path("register/",include('django.contrib.auth.urls')),
]