from django.contrib import admin
from main.models import Item, TodoList


# Register your models here.
admin.site.register(TodoList)
admin.site.register(Item)
