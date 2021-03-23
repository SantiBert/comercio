from django.views.generic import View, TemplateView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = 'index.html'


@method_decorator(login_required, name='dispatch')
class AdministrationView(TemplateView):
    template_name = 'administration.html'
