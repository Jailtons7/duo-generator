# Duplas Aleatórias

Projeto para automatizar a geração de duplas para realização
de tarefas diárias durante os dias úteis de um mês. 

As duplas são:
- geradas de forma aleatória;
- alocadas nos dias úteis do mês;
- sempre que possível,
formadas por um homem e uma mulher;

### Rodando o projeto

Antes de tudo, para ter a certeza de que os comandos abaixo 
e a aplicação irão rodar corretamente, você vai precisar do 
<strong>Python 3.8</strong> instalado na sua máquina e registrado
na variável PATH do seu SO.

<ol>
<li>Crie e ative um ambiente virtual</li>

`python -m venv venv_name`

`source venv_name/bin/activate`

<li>Instale as dependências</li>

`pip install -r requirements.txt`
<li>Crie e rode as migrations</li>

`python manage.py makemigrations`

`python manage.py migrate`

<li>Crie um super usuário</li>

`python manage.py createsuperuser`

<li>Sirva a aplicação</li>

`python manage.py runserver`

<li>Crie alguns integrantes para as duplas</li>

Basta acessar 127.0.0.1:8000/admin/duplas/integrante/add/ no seu 
navegador colocando o nome de usuário e senha criados anteriormente.

<li>Finalmente, crie as duplas</li>

Acesse 127.0.0.1:8000 marque o checkbox no canto superior e clique 
no botão "Gerar Novas Duplas"
</ol>