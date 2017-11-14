from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from pontoE.models import *
from pontoE.serializers import *
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class JustificativaViewSet(viewsets.ModelViewSet):
    queryset = Justificativa.objects.all()
    serializer_class = JustificativaSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer