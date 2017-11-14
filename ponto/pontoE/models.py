from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Horario(models.Model):
    tipo = models.CharField(max_length=100,null=True,blank=False)
    hora_Entrada = models.TimeField()
    hora_Saida = models.TimeField()

    def __str__(self):
        return '{}'.format(self.tipo)

class Funcionario(models.Model):
    nome = models.CharField(max_length=100,null=True,blank=False)
    CPF = models.CharField(max_length=11,null=True,blank=False)
    dataAniversario = models.DateField()
    user = models.ForeignKey(User,null=True,blank=False)
    horario = models.ForeignKey(Horario,null=True,blank=False)
    cargo = models.CharField(max_length=100,null=True,blank=False)

    def __str__(self):
        return '{}'.format(self.nome)

class Justificativa(models.Model):
    titulo = models.CharField(max_length=100,null=True,blank=False)
    descricao = models.TextField(max_length=240,null=True,blank=False)

    def __str__(self):
        return '{}'.format(self.titulo)

class Frequencia(models.Model):
    funcionario = models.ForeignKey(Funcionario,null=True,blank=False)
    dataHoraEntrada = models.DateTimeField()
    dataHoraSaida = models.DateTimeField()
    justificativa = models.ForeignKey(Justificativa,null=True,blank=False)
    status = models.CharField(max_length=100,null=True,blank=False)

    def __str__(self):
        return '{}'.format(self.funcionario.nome)