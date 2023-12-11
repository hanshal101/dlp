from pyexpat.errors import messages
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import FixAllocation, Teachers, TeacherAllocation
from timetable.models import TimeTableEntry
import smtplib

@login_required
@csrf_exempt
def generate_teacher_allocations(request):
    if request.method == 'POST':
        teachers = list(Teachers.objects.all())
        timetable_entries = TimeTableEntry.objects.all()

        TeacherAllocation.objects.all().delete()

        for timetable_entry in timetable_entries:
            for classroom in timetable_entry.classroom.all():
                subjects = list(timetable_entry.subjects.all())
                random.shuffle(teachers)

                for subject in subjects:
                    if teachers:
                        main_teacher = teachers.pop(0)
                        TeacherAllocation.objects.create(
                            teacher=main_teacher,
                            classroom=classroom,
                            date=subject.subjectschedule_set.first().date,
                            time=subject.subjectschedule_set.first().start_time
                        )
                    else:
                        messages.error(request, "Teachers are insufficient for the required allotment")
                        return redirect('generate_allocation_form')

        return redirect('http://127.0.0.1:8000/tt/teacherAllocated')
    
    elif request.method == 'GET':
        return render(request, 'generate_allocation_form.html')


def fixAllocation(request):
    fromaddr = "hanshal.m@somaiya.edu"
    toaddrs = "hanshalmehta785@mail.com"
    msg = "This is a test message"
    if request.method == 'POST':
        FixAllocation.objects.all().delete()

        for teachers_data in TeacherAllocation.objects.all():
            FixAllocation.objects.create(
                teacher=teachers_data.teacher,
                classroom=teachers_data.classroom,
                date=teachers_data.date,
                time=teachers_data.time
            )
            
        return render(request, 'su.html')
    
    elif request.method == 'GET':
        all_teacher_allocations = TeacherAllocation.objects.all()
        context = {'all_teacher_allocations': all_teacher_allocations}
        return render(request, 'alloc.html', context)
