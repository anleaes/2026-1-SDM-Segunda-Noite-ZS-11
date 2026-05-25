from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'contactchannels'

router = routers.DefaultRouter()
router.register('', views.ContactChannelViewSet, basename='canais-contato')

urlpatterns = [
    path('', include(router.urls)),
]
