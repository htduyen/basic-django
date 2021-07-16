# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from main.models import TodoList
from .forms import CreateNewList


def index(response, id):
    ls = TodoList.objects.get(id=id)
    return render(response, "main/list.html", dict(ls=ls))


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = TodoList(name=n)
            t.save()
        return HttpResponseRedirect(f"/{t.id}")

    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})
