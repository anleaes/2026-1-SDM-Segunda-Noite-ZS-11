from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'documents'

router = routers.DefaultRouter()
# Registra o ViewSet principal do app no router padrao.
router.register('', views.DocumentViewSet, basename='documentos')

urlpatterns = [
    path('', include(router.urls)),
]
