from os import chdir

from django.shortcuts import render
from wifi_qrcode_generator import generator

from QrCodeApp import forms


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = forms.Widget(request.POST)
        if form.is_valid():
            form.save()
            chdir('C:/Users/OMEN/Desktop/QrCode/QrCodeApp/static/QrCodeApp/')
            name = form.cleaned_data['wifi_name']
            enc = form.cleaned_data['encryption']
            parol = form.cleaned_data['password']
            qr_code = generator.wifi_qrcode(
                ssid=f'{name}', hidden=True, authentication_type=f'{enc}', password=f'{parol}'
            )
            qr_code.print_ascii()
            qr_code.make_image().save('qr.png')
    else:
        form = forms.Widget()
    return render(request, 'QrCodeApp/index.html', {'form': form})
