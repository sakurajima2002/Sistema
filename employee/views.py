from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from django.urls import reverse_lazy

from employee.forms import  Employee_Form
from employee.models import Employee

# Create your views here.

class EmployeesView(View):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        context = {
            'employees': employees,
        }
        return render(request, 'employee/employees.html', context)

class EmployeeCreateView(View):
    def get(self, request, *args, **kwargs):
        form = Employee_Form()
        context = {
            'form': form
        }
        return render(request, 'employee/createEmployee.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = Employee_Form(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('employee:employees')
        context = {
            'form': form
        }
        return render(request, 'employee/createEmployee.html', context)

class EmployeeDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        employee = get_object_or_404(Employee, pk=pk)
        context = {
            'employee': employee
        }
        return render(request, 'employee/detailEmployee.html', context)

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'email', 'salary', 'phone', 'dni', 'employee_area', 'image']
    template_name = "employee/updateEmployee.html"
    
        
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('employee:detail', kwargs={'pk': pk})

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/deleteEmployee.html'
    success_url = reverse_lazy('employee:employees')

