 
1. No terminal de comando verifique:
 Instalação python:python --version
 Instalação pip: pip --version 
    Se necessário atualize: python -m pip install --upgrade pip 


2. criando ambiente
    Livraria:  python -m venv livraria .
    Seleciona a pasta: cd .\livraria\ 
    ativa o venv: .\Scripts\activate

3. criando projeto livraria 
    Criando com Django: django-admin startproject livraria .

4. instalando django:  pip install Django 
    Confirmar funcionamento : python manage.py runserver
    (devolve March 25, 2024 - 15:12:01
    Django version 5.0.3, using settings 'livraria.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.)

------------------------

Requirements

Para instalar todos as bibliotecas 

Entrar no ambiente virtual, e depois 
```
pip install -r requirements.txt
```

Para atualizar os requirements

Entrar no ambiente virtual, e depois 
```
pip freeze > requirements.txt
```
