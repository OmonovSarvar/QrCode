from django import forms

from .models import QrCodeCreator


class Widget(forms.ModelForm):
    class Meta:
        model = QrCodeCreator
        fields = ['wifi_name', 'encryption', 'password']
        widgets = {
            'password': forms.PasswordInput({'type': 'password'})
        }
