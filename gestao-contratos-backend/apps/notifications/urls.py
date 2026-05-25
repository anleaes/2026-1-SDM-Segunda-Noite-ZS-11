from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'notifications'

router = routers.DefaultRouter()
router.register('', views.NotificationViewSet, basename='notificacoes')

urlpatterns = [
    path('', include(router.urls)),
]
