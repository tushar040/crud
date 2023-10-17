from django import forms

from . import dynamic
from .models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import re

from curd.models import Todo
from curd.models import Product
from curd.models import Category
from curd.models import Student
from curd.models import EmployeeDetails
from curd.models import studentform



def studentform(request):
    return render(request,'studentform.html')

def insertData(request):

    in1 = Student()
    data = request.POST

    in1.f_name = data.get('f_name')
    in1.l_name = data.get('l_name')
    in1.email = data.get('email')
    name_regex = r'[A_Za-z]{3,20}'

    if  in1.f_name and not re.search(name_regex, in1.f_name):
        return HttpResponse("Enter Valid Name")

    else:
        in1.save()



    return HttpResponse("<h1>GREAT IT'S WORKING NOW CHECK INFO</h1>")


def info(request):
    info = Student.objects.all()
    context = {"info": info}

    return render(request, "info.html", context)


def student(request):
    return render(request, "student.html")
def employees(request):
    employees = EmployeeDetails.objects.all()
    context = {"employees": employees}

    return render(request, "employees.html", context)
def addemp(request):
    emp = EmployeeDetails()
    data = request.POST

    emp.f_name = data.get('f_name')
    emp.l_name = data.get('l_name')
    emp.Gender = data.get('Gender')
    emp.Ride = request.POST.getlist('Ride[]')
    emp.Emp_ID = data.get('Emp_ID')
    emp.phone = data.get('phone')
    emp.Des = data.get('Des')
    emp.save()
    return HttpResponse("<h1>GREAT IT'S WORKING NOW CHECK EMPLOYEES</h1>")

def addstud(request):
    work = Student()
    data = request.POST
    files = request.FILES
    work.f_name = data.get('f_name')
    work.l_name = data.get('l_name')
    work.email = data.get('email')
    work.password = data.get('password')
    work.gender = data.get('gender')
    work.ride = request.POST.getlist('ride[]')
    work.color = request.POST['color']
    work.file = files['file']
    work.mobile = data.get('mobile')

    work.save()

    return HttpResponse("<h1>GREAT IT'S WORKING NOW CHECK STUD</h1>")

def stud(request):
    stud = Student.objects.all()
    context = {"stud": stud}

    return render(request, "stud.html", context)
def home_view1(request,*args, **kwargs):
    x = []
    for i in range(9):
        x.append(i)
    return HttpResponse("<h1>WELCOME TO MY SITE</h1>The Digits are {0}".format(x))


def showData(request):

    data1 = Todo.objects.all()

    context = {"todos": data1}

    return render(request,'show.html', context)

def deleterecord(request,id):

    instance = Todo.objects.get(id=id)
    instance.delete()

    return redirect(dynamic.urls+'show')

def deleteproduct(request,id):
    instance = Product.objects.get(id=id)
    instance.delete()

    return redirect(dynamic.urls+'showproduct')

def deletecategory(request,id):
    instance = Category.objects.get(id=id)
    instance.delete()

    return redirect(dynamic.urls+'showcat')
def showcat(request):
    data3 = Category.objects.all()

    context = {"cat": data3}
    return render(request,"showcategory.html", context)

def updatecat(request,id):
    instance = Category.objects.get(id=id)
    context = {"update": instance}

    return render(request,"updatecat.html", context)


def updaterecord(request, id):
    name = request.POST['Category_Name']
    description = request.POST['Description']
    member = Category.objects.get(id=id)
    member.Category_Name = name
    member.Description = description
    member.save()

    return redirect(dynamic.urls+'showcat')
def update(request):
    data4 = Category.objects.all()
    context = {"update": data4}

    return render(request,"updatecat.html", context)

def addcat(request):
    return render(request,"addcategory.html")
def addproduct(request):
    return render(request,"addproduct.html")
def showproduct(request):
    data2 = Product.objects.all()

    context = {"products": data2}
    return render(request,"showproduct.html", context)

def form(request):
    return render(request,"form.html")


def createData(request):
    todos = Todo()
    data = request.POST

    todos.task = data.get('task')
    todos.status = "completed"

    todos.save()
    return HttpResponse("Data Done",form)


def addData(request):
    if request.method == "POST":
        form = Todo(request.POST)
        instance = form.save()
        instance.save()

    return render(request, 'add.html')

def showByid(request,id):
    data = {
        'title':"show detail oage",
        'data':["Product1","Product2","Product3","Product4"]
    }
    return render (request,"detail.html", data)

def dashboard(request):
    return render(request,'index.html')

def Details(request):
    return render(request,'temp.html')