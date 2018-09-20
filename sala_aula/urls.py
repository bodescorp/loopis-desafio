from django.conf.urls import include, url
from . import views

urlpatterns = [
    

url(r'^$',views.lista_alunos, name='lista_alunos'),
url(r'^/professores/$',views.lista_professor, name='lista_professor'),
url(r'^/aluno/(?P<pk>[0-9]+)/$', views.AlunoDados.as_view(), name = 'dados_aluno' ),
url(r'^/professor/(?P<pk>[0-9]+)/$', views.ProfessorDados.as_view(), name = 'dados_professor' ),

url(r'^inscrever_turma/',views.CadastroTurma.as_view(), name ='cadastro_turma'),
url(r'^cadastro_aluno', views.CadastroAluno.as_view(), name='cadastro_aluno'),
url(r'^cadastro_professor', views.CadastroProfessor.as_view(), name='cadastro_professor'),
url(r'^inscrever_sala',views.CadastroSala.as_view(), name ='cadastro_sala'),

url(r'sucesso',views.sucesso, name = 'sucesso'),
url(r'god',views.god, name = 'god'),
]