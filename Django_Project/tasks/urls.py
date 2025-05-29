from django.urls import path
from tasks.views import manager_dashboard,users_dashboard,task_test

urlpatterns = [
    path('user_dashboard/',users_dashboard),
    path('manager_dashboard/',manager_dashboard),
    path('task_test/',task_test)
]