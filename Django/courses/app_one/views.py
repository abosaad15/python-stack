from django.shortcuts import render, redirect
from .models import Course, Description
from django.contrib import messages


def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request, 'index.html', context)


def destroy(request, course_id):
    context = {
        'course' : Course.objects.get(id = course_id),
        'desc' : Description.objects.get(course_id = course_id)
    }
    return render(request, 'destroy.html', context)

def delete(request, course_id):
    c = Course.objects.get(id = course_id)
    c.delete()
    # context = {
    #     'courses' : Course.objects.all()
    # }
    return redirect(index)

def addCourse(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(index)
    else:
        course = Course.objects.create(name = request.POST['name'])
        Description.objects.create(desc = request.POST['desc'], course = course)
        return redirect(index)
