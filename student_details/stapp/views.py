from django.shortcuts import render,redirect
from django.http import HttpResponse
from stapp.models import Student
from stapp.forms import StudentReg
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout


def sign(requests):
    return render(requests, 'stapp/base.html')


def signin(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return render(request,'stapp/add.html')
        else:
            messages.error(request,"Bad Credentials")
            return redirect('/sign')
    return render(request, 'stapp/signin.html')

def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        emailaddress=request.POST['emailaddress']
        password=request.POST['password']
        con_password=request.POST['con_password']

        myuser=User.objects.create_user(username, emailaddress, con_password)
        myuser.save()

        messages.success(request, "User Added Successfully")
        return redirect("/signin")
    return render(request, 'stapp/signup.html')

def signout(request):
    return render(request, 'stapp/signout.html')



def Stu_info(request):
     data=Student.objects.all()
     stu_dict={"student_data":data}
     return render(request,'stapp/index.html',context=stu_dict)



def stu_reg(request):
    form = StudentReg()
    if request.method == 'POST':
        form = StudentReg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request, 'stapp/add.html', context={'form': form})


def stu_del(request,id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('/home')

def stu_update(request,id):
    data = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentReg(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request, 'stapp/update.html', context={'student': data})

