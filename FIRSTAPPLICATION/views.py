from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return HttpResponse("This is Homepage")


def about(request):
    return HttpResponse("This is About us page")


def homeHTML(request):
    name = "Hello"
    return render(request, 'myapp/home.html', )
