from django.shortcuts import render
from django.http import HttpResponse

# Create your views / business logic here👇.

def home_page(request):
    return HttpResponse('<h1 style="color:yellow; background-color:red; text-align:center;">This response is from view function response</h1>')
