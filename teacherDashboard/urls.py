from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('examAttendence/',views.TTExamDash,name="examAttendence"),
    path('main/',views.mainDash,name="maindash"),
    path('generateall/',views.genDash,name="gendash")
]