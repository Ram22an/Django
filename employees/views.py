from django.shortcuts import render
from employees.models import Employee
from django.http import Http404, HttpResponse
# Create your views here.


# **we create the bussiness login of any app here


def employee_detail(request,Id):
    try:
        employee=Employee.objects.get(id=Id)
        print(employee)
    except:
        raise Http404("Employee not found")
    return HttpResponse(employee.first_name)

