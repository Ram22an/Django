from django.shortcuts import render
from employees.models import Employee
from django.shortcuts import get_object_or_404
# Create your views here.


# **we create the bussiness login of any app here


def employee_detail(request,Id):
    employee=get_object_or_404(Employee,id=Id)
    context={
        'employee':employee,
    }
    return render(request,'employee_detail.html',context)

