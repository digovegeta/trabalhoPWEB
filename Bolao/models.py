from django.db import models
from django.utils import timezone


class Jogador(models.Model):
    idJogador = models.AutoField (primary_key = True)
    nomeJogador = models.CharField(max_length=50)
    login =  models.CharField(max_length=50)
    senha =  models.CharField(max_length=50)
    creditos =  models.DecimalField(decimal_places = 2, max_digits = 4)

    def __str__(self):
        return self.nomeJogador
    
class Pais(models.Model):
    idPais = models.AutoField (primary_key = True)
    nomePais = models.CharField(max_length=32)
    siglaPais = models.CharField(max_length=3)
    arquivoDeImagem = models.FileField()

    def __str__(self):
        return self.nomePais

class Partida(models.Model):
    idPartida = models.AutoField (primary_key = True)
    tituloPartida = models.CharField(max_length=7)
    idPais1 = models.ForeignKey('Pais', on_delete=models.CASCADE, related_name='pais_1') 
    idPais2 = models.ForeignKey('Pais', on_delete=models.CASCADE, related_name='pais_2')
    placarPais1 = models.PositiveIntegerField(default=0)
    placarPais2 = models.PositiveIntegerField(default=0)
    resultado = models.IntegerField()
    dataInicio = models.DateTimeField(default=timezone.now)
    dataFim = models.DateTimeField(default=timezone.now)

    #def tituloPartida(self):
        #self.tituloPartida = 
      #  self.save()

    def __str__(self):
        return self.tituloPartida + ' ' + str(self.dataInicio)
    
class Aposta(models.Model):
    idAposta = models.AutoField (primary_key = True)
    idPartida = models.ForeignKey('Partida', on_delete=models.CASCADE) 
    idJogador = models.ForeignKey('Jogador', on_delete=models.CASCADE) 
    placarPais1 = models.PositiveIntegerField()
    placarPais2 = models.PositiveIntegerField()
    statusAposta = models.IntegerField()

    def __str__(self):
        return str(self.idJogador) + ' - ' + str(self.placarPais1) + ' ' + str(self.placarPais2)  + ' - ' + str(self.idPartida) 

class Login(models.Model):
    login = models.CharField(max_length=50)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.login + ' ' + self.data

# Create your models here.

