# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Aluno(models.Model):
	nome = models.CharField(
		'nome',
		max_length = 100
		)
	
	idade = models.IntegerField(
		'idade',
		)

	cpf = models.CharField(
        'cpf',
        max_length = 14
        )

	telefone = models.CharField(
        'telefone',
        max_length = 11
        )

	email = models.EmailField(
        'email',
        max_length = 254
        )

	matricula = models.CharField(
        'matricula',
        max_length = 11,
        blank = True,
        null = True
    )
	def __str__(self):
		return self.nome


class Professor(models.Model):
   	nome = models.CharField(
		'nome',
		max_length = 100
		)
	
	idade = models.IntegerField(
		'idade',
		)

	cpf = models.CharField(
        'cpf',
        max_length = 14
        )

	telefone = models.CharField(
        'telefone',
        max_length = 11
        )

	email = models.EmailField(
        'email',
        max_length = 254
        )

	matricula = models.CharField(
       	'matricula',
        max_length = 11,
        blank = True,
        null = True
    )

	materia = models.CharField(
		'materia',
		max_length = 100
		)


	def __str__(self):
		return self.nome

class Turma(models.Model):
	nome = models.CharField(
		'nome_turma',
		max_length = 100
		)

	
	def __str__(self):
		return self.nome

class Sala(models.Model):
	sala = models.ForeignKey(
		Turma,
		verbose_name = 'Turma',
		related_name = 'sala'
		)

	professor = models.ForeignKey(
		Professor,
		verbose_name = 'Professor',
        related_name = 'sala',
		)	
	
	aluno = models.ForeignKey(
		Aluno,
		verbose_name = 'Aluno',
        related_name = 'sala',
		)
	

	def __str__(self):
		return self.nome
    