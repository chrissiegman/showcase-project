from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World.")

def about(request):
    return HttpResponse("This is the about page.")

def projects(request):
    return HttpResponse("This is the projects page.")

def resumee(request):
    return HttpResponse("This is the resumee page.")

def contact(request):
    return HttpResponse("This is the contact page.")
