from django.contrib import admin

from .models import Deposito, Saque, Saldo

class DepositoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'valor', 'data', 'confirmado']
    list_filter = ['confirmado']
    search_fields = ['usuario__username']

class SaqueAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'valor', 'data', 'confirmado']
    list_filter = ['confirmado']
    search_fields = ['usuario__username']

class SaldoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'saldo_atual']
    search_fields = ['usuario__username']

admin.site.register(Deposito, DepositoAdmin)
admin.site.register(Saque, SaqueAdmin)
admin.site.register(Saldo, SaldoAdmin)
