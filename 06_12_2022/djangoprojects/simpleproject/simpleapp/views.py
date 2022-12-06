from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #msg = "message from view function"
    #return render(request,"simpleapp/home.html",{'message': msg})
    list_of_names = [{'name':'raj'},{'name':'sri'},{'name':'bob'},{'name':'tom'}]
    return render(request,"simpleapp/home.html",{'names': list_of_names})
    #return HttpResponse("<h1>Welcome to Django App</h1>")

def welcome(request):
    return HttpResponse("<h1>Welcome from view function</h1>")
