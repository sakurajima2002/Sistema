from django import forms

from employee.models import Employee

class Employee_Form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'salary', 'phone', 'dni', 'image','employee_area']