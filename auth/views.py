from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome to our data blog")

def about(request):
    return HttpResponse("this is about page")