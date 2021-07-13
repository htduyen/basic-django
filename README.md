# Chapter 1: Setup 
[Src: https://www.techwithtim.net/tutorials/django/setup/]


**Install**:    pip install django

**Create project**:     django-admin startproject name_of_project 

**Start project**:  python manage.py runserver <port_number|default=80>

**Creating an App**:    python manage.pt startapp main (same dir with project)

# Chapter 2: Datebase


Modifying settings.py

    INSTALLED_APPS = [
        **,
        'main.apps.MainConfig', # <- add this
    ]

Migrations:

    cmd:    python manage.py migrate

Defining Models and Making Migrations:

    python manage.py makemigrations main
    
    python manage.py migrate

Working With Our Database:

    $ python manage.py shell

    from main.models import Item, ToDoList # import will be different depending on script location

    list1 = ToDoList(name="Tim's List")  # create a ToDoList 
    
    list1.save()  # saves the ToDoList in the database
    
    print(list1.id)  # prints 1, each list is given an id automatically
    
    print(ToDoList.objects.all())  # prints all of the ToDoLists in the database
    
    find_list = ToDoList.objects.get(name="Tim's list")  # gets the ToDoList object(s) with name "Tim's List"
    
    # Since we defined a relationship between Item and ToDoList each ToDoList has an "item_set"
    
    print(list1.item_set.all())  # get all of the items on a ToDoList
    
    list1.create(text="Go to the mall", complete=False)  # add an item to the ToDoList
    
    list1.name = "new name"  # change the name of the list
    
    list1.save()  # save changes
    
    list1.delete()  # delete the list

