from django import forms
from .models import Social


class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ['link']
        widgets = {'link': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Link'}), }
        labels = {
            'link': '',
        }
