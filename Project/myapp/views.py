from django.shortcuts import render
from django.http import HttpResponse
import pickle
from .models import User, HealthDetails


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

def register(request):
    if request.method=="POST":
        print("I'm coming from register_form")
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        a = User(age=age, gender=gender, name=name, email=email, password=password)
        a.save()

    print("Logged in user ID is ")
    print(request.session['user_id'])
    logged_in_user = User.objects.get(id=request.session['user_id'])

    return render(request,"myapp/registration_form.html", {
        "name":logged_in_user.name    })

def update_health_details(request):
    # if request.session['user_id'] is None:
    #     return HttpResponse("Please log in first to update the details")

    if request.method=="POST":    
        Age = int(request.POST.get('Age'))
        Pregnancies = int(request.POST.get('Pregnancies'))
        Glucose = int(request.POST.get('Glucose'))
        BloodPressure = int(request.POST.get('BloodPressure'))
        SkinThickness = int(request.POST.get('SkinThickness'))
        Insulin = int(request.POST.get('Insulin'))
        BMI = int(request.POST.get('BMI'))
        DiabetesPedigreeFunction = int(request.POST.get('DiabetesPedigreeFunction'))

        user_logged_in_id = request.session['user_id']
        user_logged_in = User.objects.get(pk=user_logged_in_id)
        health_details = HealthDetails(
            user = user_logged_in,
            age = Age,
            pregnancies = Pregnancies,
            glucose = Glucose,
            blood_pressure = BloodPressure,
            skin_thickness = SkinThickness,
            insulin = Insulin,
            bmi = BMI,
            diabetes_pedigree_function = DiabetesPedigreeFunction,
            is_diabetic = 0
        )

        health_details.save()

        return HttpResponse("User details saved")
        
    return render(request, "myapp/update_health_details.html")

def login(request):
    error_message = None
    
    if request.method=="POST":
        print("I'm coming from login_form")
        email = request.POST.get('email')
        password = request.POST.get('password')

        list_users=User.objects.filter(email=email)

        # In case where the email is not present in the DB, list_users would be empty and list_users.first() 
        # and in that case user below would be None

        user=list_users.first()
        # print(user)
        # print(user.email)
        # print(user.password)
        # print(user.name)
        # print(user.age)
        # print(user.gender)
        if user is not None:
            if password==user.password:
                request.session["user_id"]=user.id
                return render(request, "myapp/login_success.html",)
            else:
                error_message = "Invalid Password!"
        else:
            error_message = "User does not exist"

    error = {
        "error_message":error_message
    }

    print(error_message)

    return render(request,"myapp/login_form.html", error)

def logout(request):
    del request.session["user_id"]
    return render(request,"myapp/login_form.html")

def submit_form(request):
    # symptoms = request.POST.get('symptoms')
    # gender = request.POST.get('gender')

    # petallength = request.POST.get('petallength')
    # petalwidth = request.POST.get('petalwidth')
    # sepallength = request.POST.get('sepallength')
    # sepalwidth = request.POST.get('sepalwidth')
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

#https://github.com/Showblown/django-project
