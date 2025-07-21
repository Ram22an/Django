from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee
def home(request):
    employees=Employee.objects.all()
    # **every model have objects it is object oriented mapping

    # **print(employees)
    # **this will print the employees in the console

    # **to send it in the html template
    context={'employees':employees,}
    # **this is a dictionary that will be passed to the template

    # return HttpResponse('')
    # **this simply return some html code

    # **this renders a whole template 
    return render(request,'home.html',context)

