from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'contracts'

router = routers.DefaultRouter()
# Registra o ViewSet principal do app no router padrao.
router.register('', views.ContractViewSet, basename='contratos')

urlpatterns = [
    path('', include(router.urls)),
]
