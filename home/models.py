from django.db import models

# Create your models here.

class StudentModel(models.Model):
    student_name = models.CharField(max_length=255)
    student_age  = models.IntegerField()

    def __str__(self):
        return self.student_name
