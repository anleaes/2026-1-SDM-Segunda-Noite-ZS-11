from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'persons'

router = routers.DefaultRouter()
# Registra o ViewSet principal do app no router padrao.
router.register('', views.PersonViewSet, basename='pessoas')

# Expoe as rotas geradas pelo router para inclusao no projeto.
urlpatterns = [
    path('', include(router.urls)),
]
