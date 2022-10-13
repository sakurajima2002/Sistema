from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from django.urls import reverse_lazy

from boss.models import Boss
from boss.forms import Boss_Form

# Create your views here.

class BossesView(View):
    def get(self, request, *args, **kwargs):
        bosses = Boss.objects.all()
        context = {
            'bosses': bosses,
        }
        return render(request, 'boss/bosses.html', context)

class BossCreateView(View):
    def get(self, request, *args, **kwargs):
        form = Boss_Form()
        context = {
            'form': form
        }
        return render(request, 'boss/createBoss.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = Boss_Form(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('boss:bosses')
        context = {
            'form': form,
        }
        return render(request, 'boss/createBoss.html', context)

class BossDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        boss = get_object_or_404(Boss, pk=pk)
        context = {
            'boss': boss
        }
        return render(request, 'boss/detailBoss.html', context)

class BossUpdateView(UpdateView):
    model = Boss
    fields = ['first_name', 'last_name', 'email', 'salary', 'phone', 'dni', 'image', 'boss_area']
    template_name = 'boss/updateBoss.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('boss:detail', kwargs={'pk': pk})

class BossDeleteView(DeleteView):
    model = Boss
    template_name = 'boss/deleteBoss.html'
    success_url = reverse_lazy('boss:bosses')