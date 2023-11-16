from django.contrib import admin
from .models import *

class SubjectScheduleInline(admin.TabularInline):
    model = SubjectSchedule
    extra = 1  # Number of empty forms to display

@admin.register(TimeTableEntry)
class TimeTableEntryAdmin(admin.ModelAdmin):
    inlines = [SubjectScheduleInline]

@admin.register(SubjectSchedule)
class SubjectScheduleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Year)
admin.site.register(Class)
admin.site.register(Subject)


admin.site.register(Teachers)