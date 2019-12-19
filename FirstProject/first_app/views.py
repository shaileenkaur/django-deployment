from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def newTemp(request):
    return render(request,'first_app/new.html')

def showForm(request):
    return render(request,'first_app/form.html')