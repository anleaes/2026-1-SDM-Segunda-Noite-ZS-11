from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
path('pessoas/', include('persons.urls', namespace='persons')),
path('canais-contato/', include('contactchannels.urls', namespace='contactchannels')),
path('clientes/', include('clients.urls', namespace='clients')),
path('funcionarios/', include('employees.urls', namespace='employees')),
path('usuarios/', include('useraccounts.urls', namespace='useraccounts')),
path('categorias-contrato/', include('contractcategories.urls', namespace='contractcategories')),
path('servicos/', include('services.urls', namespace='services')),
path('contratos/', include('contracts.urls', namespace='contracts')),
path('itens-contrato/', include('contractitems.urls', namespace='contractitems')),
path('pagamentos/', include('payments.urls', namespace='payments')),
path('documentos/', include('documents.urls', namespace='documents')),
path('notificacoes/', include('notifications.urls', namespace='notifications')),
path('auditorias/', include('audits.urls', namespace='audits')),
    path('token-autenticacao/', obtain_auth_token),
]
