from __future__ import unicode_literals

from django import forms
from sala_aula.models import Aluno, Professor, Turma, Sala

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ('__all__')

class ProfessorForm(forms.ModelForm):
	
	class Meta:
		model = Professor
		fields = ('__all__')

class TurmaForm(forms.ModelForm):
	class Meta:
		model = Turma
		fields = ('__all__')

class SalaForm(forms.ModelForm):
	class Meta:
		model = Sala
		fields = ('__all__')