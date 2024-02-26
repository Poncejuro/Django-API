from django.db import models

# Create your models here.
class CryptoCurrency(models.Model):
    ID = models.AutoField(primary_key=True)
    name=models.CharField(max_length=500)
    image=models.CharField(max_length=500)



class CryptoCurrencyHistory(models.Model):
    ID = models.AutoField(primary_key=True)
    currency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE, null= True)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)