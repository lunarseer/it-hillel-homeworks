from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random

from faker import Faker
from .models import Student, Group, Teacher


def validate_count(count):
    if isinstance(count, str):
        try:
            return int(count)
        except ValueError:
            return 0
    if isinstance(count, int):
        return count
    if isinstance(count, float):
        return int(count)


# Create your views here.


def get_students(request):
    response = [x.values() for x in Student.objects.all()] or "Not Found"
    return HttpResponse(response)

def get_groups(request):
    response = [x.values() for x in Group.objects.all()] or "Not Found"
    return HttpResponse(response)

def get_teachers(request):
    response = [x.values() for x in Teacher.objects.all()] or "Not Found"
    return HttpResponse(response)


def generate_student(request):
    gen = Faker()
    stud = Student.objects.create(firstname=gen.first_name(),
                                lastname=gen.last_name(),
                                age=random.randint(16, 52))
    # print(stud.values())
    return HttpResponse(str(stud.values()))


@csrf_exempt    #CSRF TOKEN DECORATOR, I DUNNO BUT IT HELPS HANDLE POST REQUESTS
def generate_students(request):
    
   
    gen = Faker()
    if request.method != "POST":
        responce = "{} method not implemented".format(request.method)
    if request.method == "POST":
        count = validate_count(request.POST.get('count', 0))
        # print(count)
        if count > 0:
            students = []
            for _ in range(count):
                stud = Student.objects.create(firstname=gen.first_name(),
                                            lastname=gen.last_name(),
                                            age=random.randint(16, 52))
                students.append(stud)
            responce = [x.values() for x in students]
        else:
            return HttpResponse("Wrong Count Value")
    
    return HttpResponse(responce)


@csrf_exempt
def generate_teachers(request):
    gen = Faker()
    if request.method != "POST":
        responce = "{} method not implemented".format(request.method)
    if request.method == "POST":
        count = validate_count(request.POST.get('count', 0))
        if count > 0:
            students = []
            for _ in range(count):
                stud = Teacher.objects.create(firstname=gen.first_name(),
                                            lastname=gen.last_name(),
                                            age=random.randint(16, 52))
                students.append(stud)
            responce = [x.values() for x in students]
        else:
            return HttpResponse("Wrong Count Value")
    
    return HttpResponse(responce)


@csrf_exempt
def generate_groups(request):
    if request.method != "POST":
        responce = "{} method not implemented".format(request.method)
    if request.method == "POST":
        count = validate_count(request.POST.get('count', 0))
        if count > 0:
            groups = []
            for i in range(count):
                group = Group.objects.create(name=f"group_{i}",
                )
                groups.append(group)
            responce = [x.values() for x in groups]
        else:
            return HttpResponse("Wrong Count Value")
    
    return HttpResponse(responce)