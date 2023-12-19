from collections import Counter
from itertools import count
from django.shortcuts import render,redirect
import random
import student_data
from .models import *
from student_data.models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


@login_required
@csrf_exempt
def stdAllocation(request):
    if request.method == "POST":
        Student.objects.all().delete()
        StudentAllocation.objects.all().delete()
        
        year_instance = Year.objects.get(year='SY')
        timetable_entries = TimeTableEntry.objects.filter(year=year_instance)
        class_names = timetable_entries.values_list('classroom__name', flat=True).distinct()

        roll_number_counter = 1

        for class_name in class_names:
            current_class = Class.objects.get(name=class_name)
            available_seats = current_class.capacity

            last_allocated_roll_no = Student.objects.filter(class_assigned=current_class).order_by('-roll_no').first()

            if last_allocated_roll_no:
                start_roll_no = last_allocated_roll_no.roll_no + 1
            else:
                start_roll_no = roll_number_counter

            students_to_allocate = min(available_seats, year_instance.students - start_roll_no + 1)

            end_roll_no = start_roll_no + students_to_allocate - 1

            for i in range(start_roll_no, end_roll_no + 1):
                if not Student.objects.filter(roll_no=i, class_assigned=current_class).exists():
                    student = Student.objects.create(roll_no=i, class_assigned=current_class)


            subject_schedule = SubjectSchedule.objects.filter(timetable_entry__in=timetable_entries)

            for sub in subject_schedule.filter(timetable_entry__classroom=current_class):
                allocation = StudentAllocation.objects.create(
                    classroom=current_class,
                    date=sub.date,
                    time=sub.start_time,
                    start_rollno=start_roll_no,
                    end_rollno=end_roll_no
                )
                print(allocation)

            print(f"Class: {class_name}, Seats Allocated: {students_to_allocate}, Roll Numbers: {start_roll_no} to {end_roll_no}")
            roll_number_counter = end_roll_no + 1

        return redirect('showStdAllocation')
    return render(request,'std_alloc_form.html')



def showStdAllocation(request):
    context = {'all_student_allocations':StudentAllocation.objects.all()}
    return render(request,'std_alloc.html',context)
