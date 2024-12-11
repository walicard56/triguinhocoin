from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='user_logout'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('verify_signature/', views.verify_signature, name='verify_signature'),
    path('surveys/', views.survey_view, name='survey_view'),
    path('saldo/', views.saldo_view, name='saldo'),
    path('deposito/', views.deposito_view, name='deposito'),
    path('saque/', views.saque_view, name='saque'),
    path('perfil/', views.perfil, name='perfil')
]
