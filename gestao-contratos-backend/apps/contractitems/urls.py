from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'contractitems'

router = routers.DefaultRouter()
router.register('', views.ContractItemViewSet, basename='itens-contrato')

urlpatterns = [
    path('', include(router.urls)),
]
