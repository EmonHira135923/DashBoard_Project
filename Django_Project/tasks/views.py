from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def manager_dashboard(request):
    return render(request,"dashboard/manager_dashboard.html")

def users_dashboard(request):
    return render(request,"dashboard/users_dashboard.html")
    

def task_test(request):
    return render(request,"dashboard/test_static.html")