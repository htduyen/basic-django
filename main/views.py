# Create your views here.

from django.http import HttpResponse


def index(response):
    return HttpResponse("Hello World")


def v1(response):
    return HttpResponse("View 1")
