# views.py
from django.shortcuts import render, redirect
from .models import StudentData
from django.contrib import messages
import csv

def import_csv(request):
    message = {"message":"Not added"}
    if request.method == 'POST':
        delte_data = StudentData.objects.all()
        delte_data.delete()

        csv_file = request.FILES['file']

        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        students_to_create = []
        for row in reader:
            student_instance = StudentData(
                name=row['name'],
                rollno=row['rollno'],
                email=row['email']
            )
            students_to_create.append(student_instance)

        StudentData.objects.bulk_create(students_to_create)
        
        return redirect('studentData')

    return render(request, 'import_csv.html')


def studentData(request):
    students = StudentData.objects.all().order_by('rollno').values()
    context = {'students': students}
    return render(request,'studentData.html',context)