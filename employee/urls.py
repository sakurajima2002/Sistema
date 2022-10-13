from os import pathsep
from django.urls import path
from django.contrib.auth.decorators import login_required

from employee.views import (EmployeesView,  EmployeeCreateView, EmployeeUpdateView,
                            EmployeeDetailView, EmployeeDeleteView)

app_name = 'employee'

urlpatterns = [
    path('', login_required(EmployeesView.as_view()), name='employees'),
    path('create/', login_required(EmployeeCreateView.as_view()), name='create'),
    path('<int:pk>/detail/', login_required(EmployeeDetailView.as_view()), name='detail'),
    path('<int:pk>/update/', login_required(EmployeeUpdateView.as_view()), name='update'),
    path('<int:pk>/delete/', login_required(EmployeeDeleteView.as_view()), name='delete'),
]
