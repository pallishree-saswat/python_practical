from django.shortcuts import render
from django.http import HttpResponse, response
# Create your views here.


def index(request):
    # response = HttpResponse("hello world")
    developed_by = "Pallishree Behera"
    mentors = [
        "Lucky",
        "sachin",
        "lipa",
        "ganesh"
    ]
    show_developer = True
    context = {
        "developer": developed_by,
        "mentors": mentors,
        "show_developer": show_developer
    }

    response = render(request, 'index.html', context)
    return response


def home(request):
    response = render(request, 'home.html')
    return response
