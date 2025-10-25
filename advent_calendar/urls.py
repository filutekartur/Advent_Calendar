from django.urls import path

from . import views

app_name = "adv_calendar"
urlpatterns = [
    path("",views.index,name="index"),
    path("calendar/",views.calendar,name="calendar"),
    path("day/<int:d>",views.day,name="day"),
]