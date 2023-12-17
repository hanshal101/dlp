from django.db import models
from timetable.models import *
# Create your models here.


class StudentData(models.Model):
    name = models.CharField(max_length=200)
    rollno = models.IntegerField()
    email = models.EmailField()
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    class_name = models.ForeignKey(YearClass,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name