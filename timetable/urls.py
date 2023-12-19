from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('timetable/',views.timeTable,name="timetable"),
]