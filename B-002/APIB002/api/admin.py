from django.contrib import admin
from .models import CryptoCurrency, CryptoCurrencyHistory

# Register your models here.
admin.site.register(CryptoCurrency)
admin.site.register(CryptoCurrencyHistory)
