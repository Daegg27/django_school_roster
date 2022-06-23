from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("staff/", views.list_staff),
    path("students/", views.list_students),
    path("staff/<int:employee_id>/", views.staff_detail, name="staff_detail"),
    path("students/<int:school_id>/", views.student_detail, name="student_detail")
]