from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('alloc/',views.stdAllocation,name="alloc"),
]