from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "main/index.html")
def static_view(request):
    message = "Welcome to the Quiz 2 App!"
    # Well, I would usually return HttpResponse but that is too boring!!!!
    return render(request, "main/static.html", {
        "message": message
    })
    
def list_view(request):
    shopping_list = ['apple', 'banana', 'cherry']
    return render(request, "main/list.html", {
        "ls": shopping_list
    })
    
def dynamic_view(request):
    if request.GET.get("name", '') != '':
        
        name = request.GET.get("name")
        age = request.GET.get("age")
        return render(request, "main/dynamic.html", {
            "name": name,
            "age": age if age else "Unknown"
        })    
    return render(request, "main/dynamic.html")