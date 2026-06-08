from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'audits'

router = routers.DefaultRouter()
# Registra o ViewSet principal do app no router padrao.
router.register('', views.AuditViewSet, basename='auditorias')

urlpatterns = [
    path('', include(router.urls)),
]
