from django.urls import path

from .views import hello_django, home

urlpatterns=[
    path('hello/', hello_django, name="hello"),
    path('home/', home, name="home")
]