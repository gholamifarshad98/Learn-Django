from django.urls import path
from employee import views


urlpatterns = [
    path("post-employee",views.post_Empolyee),
    path("get-employee",views.get_Employee),
    path("get-update_delete_employee/<int:pk>",views.get_update_delete_Empolyee),
]