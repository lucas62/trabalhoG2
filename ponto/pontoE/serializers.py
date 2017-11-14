from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from pontoE.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'email', 'is_staff')

    def create(self, validated_data):
       return User.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.is_staff = validated_data.get('is_staff',instance.is_staff)
        instace.save()
        return instace
        

class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horario
        fields = ('tipo','hora_Entrada','hora_Saida')
    
    def create(self, validated_data):
       return Horario.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.tipo = validated_data.get('tipo',instance.tipo)
        instance.hora_Entrada = validated_data.get('hora_Entrada',instance.hora_Entrada)
        instance.hora_Saida = validated_data.get('hora_Saida',instance.hora_Saida)
        instace.save()
        return instace

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    #user = UserSerializer(many=False)
    #horario = HorarioSerializer(many=False)
    class Meta:
        model = Funcionario
        fields = ('nome','CPF','dataAniversario','user','horario')

    def create(self,validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        funcionario = Funcionario.objects.create(**validated_data,user = user)
        return funcionario

    def update(self,instance,validated_data):
        instance.nome = validated_data.get('nome',instance.nome)
        instance.CPF = validated_data.get('CPF',instance.CPF)
        instance.dataAniversario = validated_data.get('dataAniversario',instance.dataAniversario)
        instance.user = validated_data.get('user',instance.user)
        instace.horario = validated_data.get('horario',instace.horario)
        instace.save()
        return instace


class JustificativaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Justificativa
        fields = ('titulo','descricao')
    
    def create(self, validated_data):
       return Justificativa.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.titulo = validated_data.get('titulo',instance.titulo)
        instance.descricao = validated_data.get('descricao',instance.descricao)
        instace.save()
        return instace

class FrequenciaSerializer(serializers.HyperlinkedModelSerializer):
    #funcionario = FuncionarioSerializer(many=False)
    #justificativa = JustificativaSerializer(many=False)
    class Meta:
        model = Frequencia
        fields = ('funcionario','dataHoraEntrada','dataHoraSaida','justificativa','status')

    def update(self,instance,validated_data):
        instance.funcionario = validated_data.get('funcionario',instance.funcionario)
        instance.dataHoraEntrada = validated_data.get('dataHoraEntrada',instance.dataHoraEntrada)
        instance.dataHoraSaida = validated_data.get('dataHoraSaida',instance.dataHoraSaida)
        instance.justificativa = validated_data.get('justificativa',instance.justificativa)
        instace.status = validated_data.get('status',instace.status)
        instace.save()
        return instace