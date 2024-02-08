from django.urls import path
from car import views

urlpatterns = [
    path("get-person",views.person_view),
    path("get-car",views.car_view),
    path("information",views.information),

]
