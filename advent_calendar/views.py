from django.shortcuts import render
from .models import Day
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request,"advent_calendar/index.html")
@login_required
def calendar(request):
        days = Day.objects.order_by('day')
        context = {'days': days}
        return render(request,"advent_calendar/calendar.html",context)
