from django.shortcuts import render
from .models import *
# Create your views here.


def timeTable(request):
    context = {"timetables":SubjectSchedule.objects.all()}
    return render(request,'timetable.html',context)