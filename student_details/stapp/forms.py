from django import forms
from stapp.models import Student


# class Student_det(forms.Form):
#     stu_name = forms.CharField()
#     sid = forms.IntegerField()
#     dept_name = forms.CharField()
#     did = forms.IntegerField()
#     college_name = forms.CharField()
#
# from hrapp.models import Employee
# # Create your models here.

class StudentReg(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
