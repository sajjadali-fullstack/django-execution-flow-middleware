from django.shortcuts import render
from django.http import HttpResponse

# Create your views / business logic here👇.

def welcome_view(request):
    print("This line is added by view function")  # 3 op in terminal after refreshing the page
    return HttpResponse('<h1 style="color:yellow; background-color:black; text-align:center; padding:20px; border-radius:9px;">Custome MiddleWare Demo</h1>')
