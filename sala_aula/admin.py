# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Aluno, Professor, Turma, Sala

from django.utils.html import format_html
from django.core.urlresolvers import reverse

# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
	list_display = ('nome','cpf','email' )
	search_fields = ['nome','cpf' ]

admin.site.register(Aluno, AlunoAdmin)



class ProfessorAdmin(admin.ModelAdmin):
	list_display = ('nome','cpf','email' )
	search_fields = ['nome','cpf' ]

admin.site.register(Professor, ProfessorAdmin)

class TurmaAdmin(admin.ModelAdmin):
	list_display = ('nome',)
	search_fields = ['nome',]

admin.site.register(Turma, TurmaAdmin)	

class SalaAdmin(admin.ModelAdmin):
	list_display = ('sala','professor','aluno')
	search_fields = ['sala__nome','professor__nome','aluno__nome']

admin.site.register(Sala, SalaAdmin)