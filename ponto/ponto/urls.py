"""ponto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from rest_framework import routers
from django.contrib.auth.models import User
from django.conf.urls import include, url
from django.contrib import admin
from pontoE.views import *

# Routers provide an easy way o automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'funcionario', FuncionarioViewSet)
router.register(r'horario', HorarioViewSet)
router.register(r'justificativa', JustificativaViewSet)
router.register(r'frequencia', FrequenciaViewSet)

#Wire up our API using automatic URL routing
#Additionally, we include login URLs for the browsable API
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework'))
]