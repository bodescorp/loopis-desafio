from __future__ import unicode_literals

from django.shortcuts import render, redirect,get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse
import os

from sala_aula import forms
from sala_aula import models
from .models import Aluno, Professor, Turma, Sala
#from certificados import forms





#listagem de alunos e professores
def lista_alunos (request):
	alunos = Aluno.objects.all()
	return render (request, 'sala_aula/listaalunos.html',{'alunos' : alunos})


def lista_professor (request):
	professores = Professor.objects.all()
	return render (request, 'sala_aula/listaprofessor.html',{'professores' : professores})
 

#ira mostrar as infomacoes do aluno\professor expecifico pegando o seu pk
class AlunoDados(generic.DetailView):
	model = models.Aluno
	template_name = 'sala_aula/aluno.html'

	def get_object(self):
		pk = self.kwargs.get('pk')
		return get_object_or_404(models.Aluno, pk = pk)

class ProfessorDados(generic.DetailView):
	model = models.Professor
	template_name = 'sala_aula/professor.html'

	def get_object(self):
		pk = self.kwargs.get('pk')
		return get_object_or_404(models.Professor, pk = pk)


#cadastro de Professores e alunos o ".formes cuida em preencher os dados no BD"

class CadastroAluno(generic.CreateView,generic.ListView):
    model = Aluno
    template_name = 'sala_aula/cadastro_aluno.html'
    form_class = forms.AlunoForm
    success_url = reverse_lazy('sucesso')

class CadastroProfessor(generic.CreateView):
	model = Professor
	template_name = 'sala_aula/cadastro_professor.html'
	form_class = forms.ProfessorForm
	success_url = reverse_lazy('sucesso')

class CadastroTurma(generic.CreateView):
	model = Turma
	template_name = 'sala_aula/cadastro_turma.html'
	form_class = forms.TurmaForm
	success_url = reverse_lazy('sucesso')

class CadastroSala(generic.CreateView):
	model = Sala
	template_name = 'sala_aula/cadastro_sala.html'
	form_class = forms.SalaForm
	success_url = reverse_lazy('sucesso')







def sucesso(request):
	return render (request, 'sala_aula/sucesso.html', {})

def god (request):
	return render (request, 'sala_aula/super.html',{})