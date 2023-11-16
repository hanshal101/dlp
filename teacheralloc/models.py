from django.db import models
from timetable.models import *
# Create your models here.
class TeacherAllocation(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def formatted_time(self):
        return self.time.strftime('%I:%M %p')

    def formatted_duration(self):
        return f"{self.time()} to {self.time.strftime('%I:%M %p')}"
    
    def __str__(self):
        return f"Teacher: {self.teacher.teacher_name}, Class: {self.classroom.name}, Date: {self.date} Time: {self.time}"