# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from main.models import TodoList


def index(response, id):
    ls = TodoList.objects.get(id=id)
    # item = ls.item_set.get(id=2)
    return render(response, "main/list.html", dict(ls=ls))


def home(response):
    return render(response, "main/home.html")
