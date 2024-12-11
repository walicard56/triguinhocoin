from .models import Saldo

def saldo_context_processor(request):
    if request.user.is_authenticated:
        try:
            saldo = Saldo.objects.get(usuario=request.user)
        except Saldo.DoesNotExist:
            saldo = None
    else:
        saldo = None
    return {'saldo': saldo}
