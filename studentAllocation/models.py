from django.db import models
from timetable.models import *
# Create your models here.


class StudentAllocation(models.Model):
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    start_rollno = models.IntegerField()
    end_rollno = models.IntegerField()
    def __str__(self):
        return f"Classroom: {self.classroom.name}, Date: {self.date}, Time: {self.time}, Roll Numbers: {self.start_rollno} to {self.end_rollno}"

class Student(models.Model):
    roll_no = models.IntegerField(unique=True)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"Student {self.roll_no} in {self.class_assigned}"