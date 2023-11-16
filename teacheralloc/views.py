from django.views.decorators.csrf import csrf_exempt
import random
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from timetable.models import *

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
                        allocation_main_teacher = TeacherAllocation.objects.create(
                            teacher=main_teacher,
                            classroom=classroom,
                            date=subject.subjectschedule_set.first().date,
                            time=subject.subjectschedule_set.first().start_time
                        )
                    else:
                        return HttpResponse("Teachers are insufficient for the required allotment")

        all_teacher_allocations = TeacherAllocation.objects.all()
        context = {'all_teacher_allocations': all_teacher_allocations}
        

        return render(request, 'alloc.html', context)


    return render(request, 'generate_allocation_form.html')
