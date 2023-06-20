from django.shortcuts import render
from django.http import HttpResponse
import pickle


# Create your views here.
def hello_django(request):
    print(request) 
    # while True:
    #     print("Hello")
    # the browser will keep loading ths tab if the above code is uncommented
    return HttpResponse("Hello django")

def home(request):
    data={
        "name":"josh"
    }
    return render(request,"myapp/home.html", data)

# Two types of requests on a website:
#   1. Get (To view the content and not submit any data)
#   2. Post (To view the content and submitting data in the form of email, password)

#   Age, Gender -> They make POST request on the website
#   The website responds in the form of Yes or No

def predictions(request):
    return render(request,"myapp/predictions.html")

def diabetes(request):
    return render(request,"myapp/diabetes.html")

def submit_form(request):
    # symptoms = request.POST.get('symptoms')
    # gender = request.POST.get('gender')

    # petallength = request.POST.get('petallength')
    # petalwidth = request.POST.get('petalwidth')
    # sepallength = request.POST.get('sepallength')
    # sepalwidth = request.POST.get('sepalwidth')
    a = request.POST.get('Age')
    print(a)
    print(type(a))
    print(int(a))
    while True:
        pass
    Age = int(request.POST.get('Age'))
    Pregnancies = int(request.POST.get('Pregnancies'))
    Glucose = int(request.POST.get('Glucose'))
    BloodPressure = int(request.POST.get('BloodPressure'))
    SkinThickness = int(request.POST.get('SkinThickness'))
    Insulin = int(request.POST.get('Insulin'))
    BMI = int(request.POST.get('BMI'))
    DiabetesPedigreeFunction = int(request.POST.get('DiabetesPedigreeFunction'))

    inputdata = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

    # input_data = [sepallength, sepalwidth, petallength, petalwidth]

    # with open(r"C:\Users\showb\OneDrive\Desktop\Newproject\Project\machine_learning_models\iris_model.pickle") as f:
    #     model = pickle.load(f)

    with open(r"C:\Users\showb\OneDrive\Desktop\Newproject\Project\machine_learning_models\diabetes_model.pickle", "rb") as f:
        diamodel = pickle.load(f)

    # print(model.predict([input_data]))

    diaoutcome = diamodel.predict([inputdata])

    print(diaoutcome)
    
    data = {
    "outcome":diaoutcome[0]
    }

    # data={
    #        "symptoms":symptoms,
    #        "gender":gender
    # }
    # This model object is actually from the Jupyter Notebook
    # model_smoke.pickle
    # How we can get in this Python File is through unpickling it from pickled file.
    # predict = model.predict([age, gender])

    # return render(request, "myapp/submit_form.html", data)
    # 
    # return HttpResponse(f"Age: {age} Gender: {gender}")

    return render(request,"myapp/welcome.html", data)

    # class car:
    #     def __init__(self, carlength, mileage):
    #         pass

    
    # a = car(self)
    # a.carlength


    
    

def demo(request):

    # fruits=["banana", "orange", "strawberry"]
    # data={
    #     "fruits":fruits
    # }

    peoples = [
        {'name': 'ABC', 'age': 19},
        {'name': 'df', 'age': 91},
        {'name': 'vgsd', 'age': 39},
        {'name': 'dbvhd', 'age': 14}
    ]
    vegetables = [
        'brocolli', 'carrot', 'lettuce'
    ]

    data = {
        'peoples': peoples,
        'vegetables': vegetables
    }

    return render(request,"myapp/demo.html", data)

#https://github.com/Showblown/django-projec
