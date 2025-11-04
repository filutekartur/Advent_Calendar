from django.shortcuts import render,redirect
from .models import Day
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.


def index(request):
    return render(request,"advent_calendar/index.html")
@login_required
def calendar(request):
        days = Day.objects.order_by('day')
        context = {'days': days}
        return render(request,"advent_calendar/calendar.html",context)
@login_required
def day(request,d):
        #if(0):
        if(d>timezone.now().day and request.user.username != 'admin'): # correct if statement: uncomment on production enviroment
                return redirect("adv_calendar:calendar")
        else:
                day = Day.objects.get(day=d)
                if request.user.username !='admin' and not day.open_date:
                       day.open_date = timezone.now()
                       day.save()
                context = {'day': day}
                return render(request,"advent_calendar/day.html",context)
@login_required
def review(request):
        if request.user.username == 'admin':
                days = Day.objects.order_by('day')
                context = {'days': days}
                return render(request,"advent_calendar/review.html",context)
        else:
               return redirect("adv_calendar:indes")