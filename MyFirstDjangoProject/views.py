from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Welcome to My First Django Project!</h1>")

