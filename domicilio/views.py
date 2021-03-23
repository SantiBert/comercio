from django.views.generic import View, UpdateView
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import Address
from .forms import AddressForm


@method_decorator(login_required, name='dispatch')
class AdminAddressUpdateView(UpdateView):
    model = Address
    template_name = 'addres_update_form.html'
    form_class = AddressForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('address')


@method_decorator(login_required, name='dispatch')
class AdminAddressView(View):
    def get(self, request, *args, **kwargs):
        address = Address.objects.all().order_by('-created_date')
        context = {
            'address': address[0]
        }
        return render(request, 'addres_admin.html', context)
