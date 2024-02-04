from django.urls import path
from myApp import views


urlpatterns = [
    path("helloworld",views.helloWorld),
    path("hello", views.hello),
    path("claculator", views.calculator)

]