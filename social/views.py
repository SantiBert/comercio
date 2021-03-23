from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from .models import Social
from .forms import SocialForm


@method_decorator(login_required, name='dispatch')
class SocialListView(ListView):
    template_name = 'social_list.html'
    model = Social
    context_object_name = 'socials'


@method_decorator(login_required, name='dispatch')
class SocialUpdateView(UpdateView):
    model = Social
    template_name = 'social_update_form.html'
    form_class = SocialForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('socialList')
