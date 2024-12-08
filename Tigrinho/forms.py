from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'e-mail'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'senha'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirmar a senha'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms
from .models import Deposito, Saque

class DepositoForm(forms.ModelForm):
    class Meta:
        model = Deposito
        fields = ['valor']

from django import forms
from .models import Saque

from django import forms
from .models import Saque

class SaquePixForm(forms.ModelForm):
    class Meta:
        model = Saque
        fields = ['valor']
        widgets = {
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o valor para saque via Pix',
                'min': '0',
                'step': '0.01'
            }),
        }
        labels = {
            'valor': 'Valor do Saque (R$)',
        }

class SaqueCriptoForm(forms.ModelForm):
    class Meta:
        model = Saque
        fields = ['valor']
        widgets = {
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o valor para saque via Criptomoeda',
                'min': '0',
                'step': '0.01'
            }),
        }
        labels = {
            'valor': 'Valor do Saque (Cripto)',
        }


