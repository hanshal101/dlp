from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('generate-alloc/',views.stdAllocation,name="generate-alloc"),
    path('alloc/',views.showStdAllocation,name="showStdAllocation"),
]