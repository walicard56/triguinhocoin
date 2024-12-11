# Tigrinho/models.py

from django.db import models
from django.contrib.auth.models import User

class Deposito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.usuario} - {self.valor}'

class Saque(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.usuario} - {self.valor}'

class Saldo(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo_atual = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.usuario} - {self.saldo_atual}'