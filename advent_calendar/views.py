from django.shortcuts import render
from .models import day
# Create your views here.


def index(request):
    return render(request,"advent_calendar/index.html")
def calendar(request):
    days = day.objects.order_by('day')
    context = {'days': days}
    return render(request,"advent_calendar/calendar.html",context)