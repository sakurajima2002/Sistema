from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, DeleteView
from django.urls import reverse_lazy

from workArea.forms import Work_Area_Form
from workArea.models import Work_Area

# Create your views here.

class WorkAreaView(View):
    def get(self, request, *args, **kwargs):
        workAreas = Work_Area.objects.all()
        form = Work_Area_Form()
        context = {
            'workAreas': workAreas,
            'form': form,
        }
        return render(request, 'workArea/workAreas.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = Work_Area_Form(request.POST or None)
            if form.is_valid():
                form.save()        
                return redirect('workArea:workAreas')
            else:
                messages.error(request, 'Work Area already exists')
                return redirect('workArea:workAreas')
        context = {
            'form': form,
        }
        return render(request, 'workArea/workAreas.html', context)

class WorkAreaUpdateView(UpdateView):
    model = Work_Area
    fields = ['name']
    template_name = 'workArea/updateWorkArea.html'
    
    def get_success_url(self):
        return reverse_lazy('workArea:workAreas')

class WorkAreaDeleteView(DeleteView):
    model = Work_Area
    template_name = 'workArea/deleteWorkArea.html'
    success_url  = reverse_lazy('workArea:workAreas')
