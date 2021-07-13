# Create your views here.

from django.http import HttpResponse

from main.models import TodoList


def index(response, id):
    ls = TodoList.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse(f"Todo: {ls.name} - Item: {item}")


def v1(response):
    return HttpResponse("View 1")
