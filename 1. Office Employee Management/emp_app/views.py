from django.shortcuts import render
from django.http import HttpResponse
from . models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')

def view_emp(request):
    emp = Employee.objects.all()
    context = {
        'emp' : emp
    }
    return render(request, 'view_emp.html',context)

def add_emp(request):

    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = int(request.POST['phone'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        dept = int(request.POST['dept'])

        new_emp = Employee(first_name = first_name, last_name = last_name, salary = salary, bonus = bonus, role_id = role, dept_id = dept, phone = phone, hiredate = datetime.now())

        new_emp.save()

        return HttpResponse("<h1> New Employee Added !!! </h1>")

    elif(request.method == 'GET'):
        return render(request, 'add_emp.html')

    else:
        return HttpResponse("<h1> Error !!! </h1>")
    
def delete_emp(request, emp_id = 0):
    if(emp_id):
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()

            return HttpResponse("<h1> Employee successfully removed !!! </h1>")
        except:
            return HttpResponse("<h1> Error !!! </h1>")

    emp = Employee.objects.all()
    context = {
        'emp' : emp
    }
    return render(request, 'delete_emp.html', context)

def filter_emp(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        role = request.POST['role']
        dept = request.POST['dept']
        emp = Employee.objects.all()

        if name:
            emp = emp.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if role:
            emp = emp.filter(role__name = role)
        if dept:
            emp = emp.filter(dept__name = dept)

        context = {
            'emp' : emp
        }

        return render(request, 'view_emp.html', context)

    elif(request.method == 'GET'):
        return render(request, 'filter_emp.html')

    else:
        return HttpResponse("<h1> Error !!! </h1>")