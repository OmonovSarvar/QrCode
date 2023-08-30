from django.db import models
from django.utils import timezone


# Create your models here.

class QrCodeCreator(models.Model):
    CHOICES = (
        ('WPA', 'WPA'),
        ('WEP', 'WEP')
    )
    wifi_name = models.CharField(max_length=33)
    encryption = models.CharField(max_length=4, choices=CHOICES, default='WPA')
    password = models.CharField(max_length=33)
    begin = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return f"Ilova ishlatildi {self.begin}da"
