from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def manager_dashboard(request):
    return render(request,"manager_dashboard.html")

def users_dashboard(request):
    return render(request,"users_dashboard.html")
    

