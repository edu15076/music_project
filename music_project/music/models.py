import uuid
from django.db import models


# Create your models here.


class Gender(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = (
        (MALE, 'Man'),
        (FEMALE, 'Woman'),
        (OTHER, 'Other')
    )


class Banda(models.Model):
    nome = models.CharField(max_length=100)
    data_de_criacao = models.DateField()
    site = models.URLField()
    numero_de_premiacoes = models.IntegerField()
    estilo_musical = models.ForeignKey('EstiloMusical', on_delete=models.CASCADE)
    musicos = models.ManyToManyField('Musico')

    def __str__(self):
        return self.nome


class Musico(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=1, choices=Gender.GENDER_CHOICES)

    def __str__(self):
        return self.nome


class EstiloMusical(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
