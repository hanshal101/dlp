from collections import Counter
from itertools import count
from django.shortcuts import render
import random
import student_data
from .models import *
from student_data.models import *
from django.http import HttpResponse
# Create your views here.

from django.db import IntegrityError

def stdAllocation(request):
    Student.objects.all().delete()
    year_instance = Year.objects.get(year='SY')
    timetable_entries = TimeTableEntry.objects.filter(year=year_instance)
    class_names = timetable_entries.values_list('classroom__name', flat=True).distinct()

    # Initialize a global roll number counter
    roll_number_counter = 1

    for class_name in class_names:
        current_class = Class.objects.get(name=class_name)
        available_seats = current_class.capacity

        # Fetch the last allocated roll number for the current class
        last_allocated_roll_no = Student.objects.filter(class_assigned=current_class).order_by('-roll_no').first()

        # If students have been allocated to this class before, start from the next roll number
        if last_allocated_roll_no:
            start_roll_no = last_allocated_roll_no.roll_no + 1
        else:
            start_roll_no = roll_number_counter

        # Calculate the number of students to allocate within the class capacity
        students_to_allocate = min(available_seats, year_instance.students - start_roll_no + 1)

        end_roll_no = start_roll_no + students_to_allocate - 1

        for i in range(start_roll_no, end_roll_no + 1):
            # Check if a student with the same roll_no and class_assigned already exists
            if not Student.objects.filter(roll_no=i, class_assigned=current_class).exists():
                student = Student.objects.create(roll_no=i, class_assigned=current_class)
                
        print(f"Class: {class_name}, Seats Allocated: {students_to_allocate}, Roll Numbers: {start_roll_no} to {end_roll_no}")

        # Update the global roll number counter
        roll_number_counter = end_roll_no + 1

    return HttpResponse("Access")
