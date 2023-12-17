from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField()
    def __str__(self):
        return self.name

class Year(models.Model):
    year = models.CharField(max_length=2)
    students = models.IntegerField()

    def __str__(self) -> str:
        return self.year

class TimeTableEntry(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    classroom = models.ManyToManyField(Class)
    subjects = models.ManyToManyField(Subject, through='SubjectSchedule')

    def __str__(self):
        return f"Year: {self.year}"

class SubjectSchedule(models.Model):
    timetable_entry = models.ForeignKey(TimeTableEntry, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def formatted_time(self):
        return self.start_time.strftime('%I:%M %p')

    def formatted_duration(self):
        return f"{self.formatted_time()} to {self.end_time.strftime('%I:%M %p')}"

    def __str__(self):
        return f"Year: {self.timetable_entry.year}, Subject: {self.subject.name}, Date: {self.date}, Class: {self.timetable_entry.classroom}"


class Teachers(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=200)
    teacher_email = models.EmailField(max_length=200)
    teacher_phno = models.IntegerField()

    def __str__(self):
        return self.teacher_name
    

class YearClass(models.Model):
    yearclass = models.CharField(max_length=3)
    def __str__(self):
        return self.yearclass