from multiprocessing import context
from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'core/home.html', context)

class PrivacyPolicyView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'core/privacy.html', context)

class TermsConditionsView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'core/terms_conditions.html', context)
