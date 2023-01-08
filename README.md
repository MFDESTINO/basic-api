# Hashdex API Challenge
Projeto de API para desafio técnico  

## Dependências

- `fastapi`
- `pymongo`
- `python-dotenv`
- `pytest`

## Instalação

Primeiro crie um ambiente virtual para o projeto:

    python3 -m venv hashdex-api-challenge-venv

Em seguida, inicialize o ambiente virtual e instale as dependências necessárias:

    source hashdex-api-challlenge-venv/bin/activate
    python3 -m pip install 'fastapi[all]' 'pymongo[srv]' python-dotenv

Com as dependências instaladas, clone este repositório:

    git clone https://github.com/couto0/hashdex-api-challenge.git
    cd hashdex-api-challenge

## Métodos

### Request

`GET /thing/`

    curl -i -H 'Accept: application/json' http://localhost:8000/thing/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    []

