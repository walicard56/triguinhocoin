# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm, SaquePixForm, SaqueCriptoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='home')
def dashboard(request):
    return render(request, 'Tigrinho/dashboard.html')

def perfil(request):
    return render(request, 'Tigrinho/perfil.html')

def home(request):
    login_form = LoginForm()
    register_form = RegisterForm()

    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Login incorreto')
            else:
                messages.error(request, 'Erro no formulário de login. Verifique os dados informados.')
        elif 'register' in request.POST:
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                try:
                    register_form.save()
                    messages.success(request, 'Cadastro realizado com sucesso. Faça login.')
                    return redirect('home')
                except Exception as e:
                    messages.error(request, f'Erro ao salvar usuário: {e}')
            else:
                messages.error(request, 'Erro no cadastro. Verifique os dados informados.')
                for field, errors in register_form.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')

    return render(request, 'Tigrinho/home.html', {'login_form': login_form, 'register_form': register_form})


def user_logout(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('home')

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from eth_account.messages import encode_defunct
from web3.auto import w3
from django.contrib.auth import login
from django.contrib.auth.models import User

@csrf_exempt
def verify_signature(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        account = data['account']
        message = data['message']
        signature = data['signature']

        # Verifique a assinatura
        message_hash = encode_defunct(text=message)
        recovered_address = w3.eth.account.recover_message(message_hash, signature=signature)

        if recovered_address.lower() == account.lower():
            # Autenticar o usuário no Django
            user, created = User.objects.get_or_create(username=account)
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid signature'}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)


# views.py
from django.shortcuts import render
from .theoremreach_service import TheoremReachService
from django.conf import settings

def survey_view(request):
    user_id = request.user.id  # ou qualquer identificador de usuário que você utilize
    user_ip = request.META.get('REMOTE_ADDR')
    theoremreach = TheoremReachService()
    user_details = theoremreach.get_user_details(user_id, user_ip)
    context = {
        'user_id': user_id,
        'api_key': settings.THEOREMREACH_API_KEY,
        'surveys_available': user_details.get('surveys_available', False)
    }
    return render(request, 'Tigrinho/surveys.html', context)


# views.py

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'login_form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Saldo, Deposito, Saque
from .forms import DepositoForm

@login_required
def saldo_view(request):
    saldo, created = Saldo.objects.get_or_create(usuario=request.user)
    return render(request, 'Tigrinho/saldo.html', {'saldo': saldo})

@login_required
def deposito_view(request):
    if request.method == 'POST':
        form = DepositoForm(request.POST)
        if form.is_valid():
            deposito = form.save(commit=False)
            deposito.usuario = request.user
            deposito.save()
            return redirect('saldo')
    else:
        form = DepositoForm()
    return render(request, 'Tigrinho/deposito.html', {'form': form})


def saque_view(request):
    pix_form = SaquePixForm()
    cripto_form = SaqueCriptoForm()
    return render(request, 'Tigrinho/saque.html', {'pix_form': pix_form, 'cripto_form': cripto_form})

