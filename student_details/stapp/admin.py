from django.contrib import admin
from stapp.models import Student
# Register your models here.
class Student_data(admin.ModelAdmin):
    list=["stu_name","sid","dept_name","did","college_name",]

admin.site.register(Student, Student_data)