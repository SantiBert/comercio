from django import forms
from django.db import models
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'provorstate', 'country',
                  'zipcode', 'email', 'domicilio']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Domicilio'}),
            'provorstate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provincia o Estado'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código postal'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
        }
        labels = {
            'city': 'Ciudad', 'provorstate ': 'Provincia/Estado', 'zipcode': 'Código Postal ', 'email': 'E-mail', 'domicilio': 'Domicilio',
        }
