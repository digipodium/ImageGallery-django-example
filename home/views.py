from django.shortcuts import render
from django.http import HttpResponse


def example_fun(request):
   
    return HttpResponse("response")

def example_funny(request):
    pass