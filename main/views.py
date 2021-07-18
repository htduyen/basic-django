# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from main.models import TodoList
from .forms import CreateNewList


def index(response, id):
    ls = TodoList.objects.get(id=id)

    # ["name"], ["clicked"] ==> value abtribute in temlate
    # {"save": ["save"], "c1": ["click"]}
    if response.method == "POST":
        # print(response.POST)
        # update complete or not
        if response.POST.get("save"):
            for item in ls.item_set.all():
                # get name[c<id>] == value
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                if "text" + str(item.id) in response.POST:
                    item.text = response.POST.get("text" + str(item.id))

                item.save()
        elif response.POST.get("add"):
            newItem = response.POST.get("new")
            if newItem != "":
                ls.item_set.create(text=newItem, complete=False)
            else:
                print("invalid")
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
