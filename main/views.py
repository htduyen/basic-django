# Create your views here.

from django.http import HttpResponse


def index(response, id):
    return HttpResponse(f"ID: {id}")


def v1(response):
    return HttpResponse("View 1")
