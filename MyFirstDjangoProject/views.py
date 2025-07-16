from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse('')
    # this simply return some html code

    # this renders a whole template 
    return render(request,'home/home.html')

