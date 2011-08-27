from django.db import models

class Conta(models.Model):
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    descicao = models.CharField(max_lenght=40)
