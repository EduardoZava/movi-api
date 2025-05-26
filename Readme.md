# Movie Opinion API

API RESTful para gerenciar opiniões e avaliações de usuários sobre filmes, integrando dados da OMDb API.

## Requisitos

## Instalando Python 

sudo apt install python3-venv
venv
 
 python3 -m venv arch_venv
 source arch_venv/bin/activate
 pip install -r requirements.txt

 se der erro remova e crie novamente 
 rm -rf /home/ezava/dsv/Projetos/Achitecture_Challenge/movie-api/arch_vevv

 python3 -m venv arch_venv
 note que corrigi o nome do ambiente

 fastapi run app/main.py primeiro deu um erro pedindo para instalar fastapi standart

 RuntimeError: To use the fastapi command, please install "fastapi[standard]":

        pip install "fastapi[standard]"

 Agora novamente :

 fastapi run app/main.py

  FastAPI   Starting production server 🚀
 
             Searching for package file structure from directories with __init__.py files
             Importing from /home/ezava/dsv/Projetos/Achitecture_Challenge/movie-api/app
 
    module   🐍 main.py
 
      code   Importing the FastAPI app object from the module with the following code:
 
             from main import app
 
       app   Using import string: main:app
 
    server   Server started at http://0.0.0.0:8000
    server   Documentation at http://0.0.0.0:8000/docs
 
             Logs:
 
      INFO   Started server process [17503]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
      INFO   Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

## salva no repositorio pela primeira vez

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/EduardoZava/movi-api.git
git push -u origin main

## Docker e Docker Compose





## Chave OMDb API (http://www.omdbapi.com/)

## Configuração

Crie um arquivo `.env` na raiz do projeto:

