from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from signup.models import signup
from employee_details.models import Employee

def disp(request):
    return HttpResponse('this is a django responce')


def about(request):

    return render(request, 'about.html')

def login(request):

    return render(request, 'login.html')   

def signup(request):

    return render(request, 'signup.html')    

def sum(request):

    result=0
    try:
        num1 = int(request.GET['first'])
        num2 = int(request.GET['second'])
        result=num1+num2
    except Exception as e:
        print(e)    

    return render(request, 'sum.html', {'sum':result})     


def signup1(request):

    try:

        username= request.POST['username']
        passward= request.POST['passward']
        sg=signup(username=username, passward=passward)
        sg.save()
    
    except Exception as e:
        print(e)


    return render(request,'signup1.html')


def home(request):

    return render(request, 'employee.html')


def getAllEmp(request):
    emp=Employee.objects.all()

    data={
        'emp':emp
    }    
    
    return render(request, 'employee.html', data)


def addEmp(request):
    name=request.POST['name']    
    email=request.POST['email']
    address=request.POST['address']
    phone=request.POST['phone']

    emp=Employee(name=name, email=email, address=address, phone=phone)
    emp.save()

    return redirect('/emp/')



def editEmp(request):
    Employee.objects.all()

    data={
        'emp':emp
    }    

    return render(request,'employee.html', data)

def updateEmp(request,id):
    name=request.POST['name']    
    email=request.POST['email']
    address=request.POST['address']
    phone=request.POST['phone']

    emp=Employee(id=id, name=name, email=email, address=address, phone=phone)
    emp.save()

    return redirect('/emp/')

    return render(request,'employee.html')

    
def deleteEmp(request,id):
    emp=Employee.objects.filter(id=id).delete()    
    
    return redirect('/emp/')