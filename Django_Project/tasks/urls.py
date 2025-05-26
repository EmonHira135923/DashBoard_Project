from django.urls import path
from tasks.views import manager_dashboard,users_dashboard

urlpatterns = [
    path('user_dashboard/',users_dashboard),
    path('manager_dashboard/',manager_dashboard)
]