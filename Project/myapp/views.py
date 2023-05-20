from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_django(request):
    print(request) 
    # while True:
    #     print("Hello")
    # the browser will keep loading ths tab if the above code is uncommented
    return HttpResponse("Hello django")

def home(request):
    return render(request,"myapp/home.html")

#https://github.com/Showblown/django-projec
