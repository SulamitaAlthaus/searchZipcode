# App Consulta CEP
## Aplicativo para buscar CEPs e cadastrar endereços.

### Status do projeto: Concluído

### Features
    - Busca endereços por CEP
    - CRUD endereços

### Pré-requisitos
Antes de começar, você precisa ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Docker](https://www.docker.com/) e [Node.js](https://nodejs.org/en/).
Além disso, é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

### Rodando o Back End

#### Clone este repositório
$ git clone https://github.com/SulamitaAlthaus/searchZipcode

#### Acesse a pasta do projeto no terminal/cmd
$ cd backend

#### Crie o seu arquivo ENV
    Exemplo:
        DATABASE_HOST=db
        DATABASE_PORT=5432
        DATABASE_USER=myuser
        DATABASE_PASSWORD=mypassword
        DATABASE_NAME=searchzipcode


#### Execute a aplicação em modo de desenvolvimento
$ sudo docker-compose up

O servidor inciará na porta 8000 <http://localhost:8000>

#### Para administrar o projeto
$ sudo docker-compose exec web bash
- Crie um usuário
- $ python manage.py superuser

Acesse <http://localhost:8000/admin> para administrar o projeto

### Rodando o Front End

#### Acesse a pasta do projeto no terminal/cmd
$ cd frontend

#### Instale as dependências
$ yarn install

#### Execute a aplicação 
$ yarn dev 

A aplicação inciará na porta:5173 - acesse <http://127.0.0.1:5173/>


### Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Docker](https://www.docker.com/)
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Vue](https://www.postgresql.org/)
- [Vite](https://vitejs.dev/)

### Autor
    Sulamita Althaus 
