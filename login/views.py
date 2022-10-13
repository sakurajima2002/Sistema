from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , logout , authenticate
from django.views.generic import View

# Create your views here.

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'login/login.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'User not found')
            else:
                messages.error(request, 'Invalid username or password')
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'login/login.html', context)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')