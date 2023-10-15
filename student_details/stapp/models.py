from django.db import models



# Create your models here.
class Student(models.Model):
    stu_name=models.CharField(max_length=20)
    sid=models.IntegerField()
    dept_name=models.CharField(max_length=20)
    did=models.IntegerField()
    college_name=models.CharField(max_length=50)

    def __str__(self):
        return f"student {self.stu_name} added completely"








