from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('generate-allocations/', views.generate_teacher_allocations, name="generate_teacher_allocations"),

]