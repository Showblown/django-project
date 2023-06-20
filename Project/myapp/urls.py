from django.urls import path

from .views import hello_django, home, demo, submit_form, predictions, diabetes

urlpatterns=[
    path('hello/', hello_django, name="hello"),
    path('home/', home, name="home"),
    path('demo/', demo, name="demo"),
    path('submit/', submit_form, name="submit_form"),
    path('predictions/', predictions, name="predictions"),
    path('diabetes/', diabetes, name="diabetes")
]