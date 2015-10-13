from django.shortcuts import render, HttpResponse
from showcase_app.forms import ContactForm

def index(request):
    return render(request, 'showcase_app/index.html', {})

def about(request):
    return render(request, 'showcase_app/about.html', {})

def projects(request):
    return render(request, 'showcase_app/projects.html', {})

def resumee(request):
    return render(request, 'showcase_app/resumee.html', {})

def contact(request):
    form_class = ContactForm
    return render(request, 'showcase_app/contact.html', {'form': form_class})
