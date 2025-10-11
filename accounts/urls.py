from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("login/",views.index,name="index"),
    path("register/",views.calendar,name="calendar"),
]