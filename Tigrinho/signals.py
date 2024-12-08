from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Deposito, Saque, Saldo

@receiver(post_save, sender=Deposito)
def atualizar_saldo_deposito(sender, instance, created, **kwargs):
    if created and instance.confirmado:
        saldo, _ = Saldo.objects.get_or_create(usuario=instance.usuario)
        saldo.saldo_atual += instance.valor
        saldo.save()

@receiver(post_save, sender=Saque)
def atualizar_saldo_saque(sender, instance, created, **kwargs):
    if created and instance.confirmado:
        saldo, _ = Saldo.objects.get_or_create(usuario=instance.usuario)
        if saldo.saldo_atual >= instance.valor:
            saldo.saldo_atual -= instance.valor
            saldo.save()
        else:
            # Não permita que o saque seja confirmado se o saldo for insuficiente
            instance.confirmado = False
            instance.save()
