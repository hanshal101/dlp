from django.db import models

# Create your models here.


class StudentData(models.Model):
    name = models.CharField(max_length=200)
    rollno = models.IntegerField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name