from django.urls import path

from .views import hello_django, home, demo, submit_form, predictions, diabetes, register, login, logout, update_health_details

urlpatterns=[
    path('hello/', hello_django, name="hello"),
    path('home/', home, name="home"),
    path('demo/', demo, name="demo"),
    path('submit/', submit_form, name="submit_form"),
    path('predictions/', predictions, name="predictions"),
    path('diabetes/', diabetes, name="diabetes"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name='logout'),
    path('update_health_details', update_health_details, name = 'update_health_details')
]