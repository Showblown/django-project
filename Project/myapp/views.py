from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_django(request):
    print("Printing Request")
    print(request) 
    # while True:
    #     print("Hello")
    return HttpResponse("Hello django")

def home(request):
    return render(request,"myapp/home.html")

#https://github.com/Showblown/django-project
