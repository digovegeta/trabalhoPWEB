from django.db import models
from django.utils import timezone


class Jogador(models.Model):
    idJogador = models.AutoField (primary_key = True)
    nomeJogador = models.CharField(max_length=50)
    login =  models.CharField(max_length=50)
    senha =  models.CharField(max_length=50)
    creditos =  models.DecimalField(decimal_places = 2, max_digits = 4)
    
class Pais(models.Model):
    idPais = models.AutoField (primary_key = True)
    NomePais = models.CharField(max_length=32)
    siglaPais = models.CharField(max_length=3)
    arquivoDeImagem = models.FileField()
    

class Partida(models.Model):
    idPartida = models.AutoField (primary_key = True)
    idPais1 = models.ForeignKey('Pais', on_delete=models.CASCADE, related_name='pais_1') 
    idPais2 = models.ForeignKey('Pais', on_delete=models.CASCADE, related_name='pais_2')
    placarPais1 = models.PositiveIntegerField(default=0)
    placarPais2 = models.PositiveIntegerField(default=0)
    resultado = models.IntegerField()
    datainicio = models.DateTimeField(default=timezone.now)
    dataFim = models.DateTimeField(default=timezone.now)

    
class Aposta(models.Model):
    idAposta = models.AutoField (primary_key = True)
    idPartida = models.ForeignKey('Partida', on_delete=models.CASCADE) 
    idJogador = models.ForeignKey('Jogador', on_delete=models.CASCADE) 
    placarPais1 = models.PositiveIntegerField()
    placarPais2 = models.PositiveIntegerField()
    statusAposta = models.IntegerField()
    

# Create your models here.

