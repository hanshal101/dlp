from pyexpat.errors import messages
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import FixAllocation, Teachers, TeacherAllocation
from timetable.models import TimeTableEntry
from django.core.mail import send_mail

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
                        return HttpResponse("Teachers are insufficient for the required allotment")

        return redirect('http://127.0.0.1:8000/tt/teacherAllocated')
    
    elif request.method == 'GET':
        return render(request, 'generate_allocation_form.html')


def fixAllocation(request):

    if request.method == 'POST':
        FixAllocation.objects.all().delete()

        receiver_list = []

        for teachers_data in TeacherAllocation.objects.all():
            FixAllocation.objects.create(
                teacher=teachers_data.teacher,
                classroom=teachers_data.classroom,
                date=teachers_data.date,
                time=teachers_data.time
            )

            receiver_list.append({
            'email': teachers_data.teacher.teacher_email,
            'room': teachers_data.classroom,
            'name': teachers_data.teacher.teacher_name
        })


        subject = 'Classroom allocation and timetable'

        for recipient in receiver_list:
            to_name =recipient['name']
            to_email = recipient['email']
            class_room = recipient['room']
            message = f'To {to_email.split("@")[0]},\n hello {to_name}\n you have been allotted cr no.{class_room}.\n skibidi skibidi .'

            try:
                send_mail(subject, message, 'testdlp18@outlook.com', [to_email])
            except Exception as e:
                return HttpResponse(f'Error sending email to {to_email}: {e}')

        return render(request, 'su.html')

    elif request.method == 'GET':
        all_teacher_allocations = TeacherAllocation.objects.all()
        context = {'all_teacher_allocations': all_teacher_allocations}
        return render(request, 'alloc.html', context)
