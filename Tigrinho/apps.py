from django.apps import AppConfig


class TigrinhoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Tigrinho'


class FinanceiroConfig(AppConfig):
    name = 'Tigrinho'

    def ready(self):
        import Tigrinho.signals