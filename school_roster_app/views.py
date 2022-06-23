import re
from django.shortcuts import render

# Create your views here.
from school_roster_app.models import School # import our School class

my_school = School("Django School") # create a school instance


def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "school_templates/index.html", my_data)


def list_staff(request):
    my_data = {
        "school_staff": my_school.staff
    }

    return render(request, "school_templates/staff.html", my_data)


def staff_detail(request, employee_id):
    
    staff_mem = my_school.find_staff_by_id(employee_id)
    my_data = {
        'staff_mem':staff_mem 
    }
    
    return render(request, "school_templates/staff_detail.html", my_data)


def list_students(request):
    my_data = {
        "school_students": my_school.students
    }
    
    return render(request, "school_templates/student.html", my_data)


def student_detail(request, school_id):
    student = my_school.find_student_by_id(school_id)
    my_data = {
        "student": student
    }
    
    return render(request, "school_templates/student_detail.html", my_data)