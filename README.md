# Hashdex API Challenge
Projeto de API para desafio técnico  
Nesta API é possível criar e gerenciar usuários em um banco de dados MongoDB.

## Instalação

Primeiro crie um ambiente virtual para o projeto:

    python3 -m venv hashdex-api-challenge-venv

Em seguida, inicialize o ambiente virtual:

    source hashdex-api-challlenge-venv/bin/activate

E instale as dependências necessárias:

    python3 -m pip install 'fastapi[all]' 'pymongo[srv]' python-dotenv pytest httpx

Com as dependências instaladas, clone este repositório:

    git clone https://github.com/couto0/hashdex-api-challenge.git && cd hashdex-api-challenge



## Métodos

## **GET** `/user/`
Lista todos os usuários

### Parâmetros
Sem parâmetros

### cURL
    curl -X 'GET' \
        'http://127.0.0.1:8000/user/' \
        -H 'accept: application/json'

### Resposta
Lista de todos usuários cadastrados.

Exemplo:
#### `200 OK`
    [
    {
        "_id": "3796b4cc-0efb-4469-b9a9-cbebdfc784b3",
        "username": "MFDOOM",
        "name": "Daniel Dumile",
        "email": "mfdoom@gmail.com",
        "birthday": "1971-7-13"
    }
    ]

## **POST** `/user/`
Cria um usuário.

### Parâmetros
Sem parâmetros

### Request Body

    {
        "username": "[username]",
        "email": "[email]",
        "name": "[name]",
        "birthday": "[YYYY-MM-DD]"
    }

- `username`: Sendo composto entre 5 a 25 caracteres alfanuméricos, podendo conter `-` e `.`, contanto que não sejam no início ou no fim, e não sendo seguidos. [Obrigatório]
- `email`: Um email válido. [Obrigatório]
- `name`: Um nome. [Obrigatório]
- `birthday`: Uma data de nascimento válida no formato YYYY-MM-DD. [Obrigatório]

O nome de usuário e email devem ser únicos no banco de dados, não é possível criar dois usuários com mesmo username ou email.

Exemplo:

    {
        "username": "MFDOOM",
        "email": "mfdoom@gmail.com",
        "name": "Daniel Dumile",
        "birthday": "1971-7-13"
    }

### cURL
    curl -X 'POST' \
        'http://127.0.0.1:8000/user/' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "username": "MFDOOM",
        "email": "mfdoom@gmail.com",
        "name": "Daniel Dumile",
        "birthday": "1971-7-13"
        }'

### Resposta
Retorna usuário cadastrado caso tenha sucesso.
Exemplo:
#### `201 CREATED`
    {
        "_id": "3d0733f2-fe97-48a1-8841-1c78609286df",
        "username": "MFDOOM2",
        "name": "Daniel Dumile",
        "email": "mfdoom2@gmail.com",
        "birthday": "1971-7-13"
    }

Caso algum dos campos de cadastro seja inválido, o motivo será retornado. Exemplo:
#### `400 BAD REQUEST`
    {
        "detail": "Username MFDOOM already exists!"
    }

## **PUT** `/user/{id}`
Atualiza os dados de um usuário.

### Parâmetros

- `id`: string do id do usuário, no formato uuid4. Exemplo: `3d0733f2-fe97-48a1-8841-1c78609286df`

### Request Body

    {
        "username": "[username]",
        "email": "[email]",
        "name": "[name]",
        "birthday": "[YYYY-MM-DD]"
    }

- `username`: Sendo composto entre 5 a 25 caracteres alfanuméricos, podendo conter `-` e `.`, contanto que não sejam no início ou no fim, e não sendo seguidos. [Opcional]
- `email` Um email válido. [Opcional]
- `name`: Um nome. [Opcional]
- `birthday`: Uma data de nascimento válida no formato YYYY-MM-DD. [Opcional]

O nome de usuário e email devem ser únicos no banco de dados, não é possível criar dois usuários com mesmo username ou email.

Exemplo:

    {
        "username": "MFDOOM",
        "email": "mfdoom@gmail.com",
        "name": "Daniel Dumile",
        "birthday": "1971-7-13"
    }

### cURL
    curl -X 'PUT' \
        'http://127.0.0.1:8000/user/3d0733f2-fe97-48a1-8841-1c78609286df' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "username": "MFDOOM",
        "email": "mfdoom@gmail.com",
        "name": "Daniel Dumile",
        "birthday": "1971-7-13"
        }'

### Resposta
Retorna usuário cadastrado caso tenha sucesso. Exemplo:
#### `200 OK`
    {
        "username": "MFDOOM",
        "email": "mfdoom@gmail.com",
        "name": "Daniel Dumile",
        "birthday": "1971-7-13"
    }

Caso algum dos campos de cadastro seja inválido, o motivo será retornado. Exemplo:
#### `400 BAD REQUEST`
    {
        "detail": "Username MFDOOM already exists!"
    }

Caso o id não corresponda a nenhum usuário retorna um 404. Exemplo:
#### `404 NOT FOUND`
    {
        "detail": "User with ID 3d0733f2-fe97-48a1-8841-1c78609286df not found"
    }

## **DELETE** `/user/{id}`
Apaga um usuário.

### Parâmetros

- `id`: string do id do usuário, no formato uuid4. Exemplo: `3d0733f2-fe97-48a1-8841-1c78609286df`

### cURL

    curl -X 'DELETE' \
        'http://127.0.0.1:8000/user/3d0733f2-fe97-48a1-8841-1c78609286df' \
        -H 'accept: application/json'

### Resposta
Retorna uma mensagem de sucesso caso o usuário exista. Exemplo:
#### `200 OK`

    "User with id 3d0733f2-fe97-48a1-8841-1c78609286df deleted successfully."

Caso o id não corresponda a nenhum usuário retorna um 404. Exemplo:
#### `404 NOT FOUND`
    {
        "detail": "User with ID 3d0733f2-fe97-48a1-8841-1c78609286df not found"
    }