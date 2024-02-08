from django.urls import path
from car import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("person", views.PersonViewSet)


urlpatterns = [
    path("get-car",views.car_view),
    path("information",views.information),
]
urlpatterns+=router.urls