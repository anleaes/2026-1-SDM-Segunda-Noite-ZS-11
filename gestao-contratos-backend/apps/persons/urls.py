from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'persons'

router = routers.DefaultRouter()
router.register('', views.PersonViewSet, basename='pessoas')

urlpatterns = [
    path('', include(router.urls)),
]
