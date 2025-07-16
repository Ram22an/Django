from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome to My First Django Project!")

