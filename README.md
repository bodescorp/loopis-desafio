# loopis-desafio
sala de aula (Pofessor/aluno/turma)

# 1. Criar ambiente virtual (linux)
virtualenv django

# 2. Acessar o ambiente virtual
source django/bin/activate

#3. Instalar requirements.txt
pip install -r requirements.txt

#4.Aplicar os arquivos de Migração
pyhonn manage.py makemigrations
python manage.migrate

#6.2 Usuario admin do Django
python manage.py createsuperuser


#5. Executar Projeto
python manage.py runserver

#6. Abrir navegador
http://localhost:8000

#6.1 Cadastrar pessoal  
http://localhost:8000/god

#6.2 usuario admnin
http://localhost:8000/admin
