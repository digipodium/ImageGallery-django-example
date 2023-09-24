from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def example_fun(request):
    tasks = Task.objects.all() # SELECT * FROM Task
    response = ", ".join([task.title for task in tasks])
    return HttpResponse(response)

def example_funny(request):
    pass