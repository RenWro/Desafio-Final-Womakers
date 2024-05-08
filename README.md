<h1>Projeto Final - WoMakers Code</h1>
<h3>Squad Marie Curie + Jill Tarter</h3>

<br>
<h1> Deploy </h1>

https://paulagmborges.pythonanywhere.com

<br>
<h3>Integrantes:</h3>
<ul>
<li>Ana Paula Kelm Soares</li>
<li>Beatriz Martins Cabral</li>
<li>Carla Morais</li>
<li>Eva Luana Almeida da Silva</li>
<li>Letícia dos Santos</li>
<li>Maria Eduarda Abreu</li>
<li>Paula Borges</li>
<li>Renata Biagioni Wrobleski</li>
<li>Sarah Affonço</li>
</ul>
<h3>Divisão e organização entre os exercícios:</h3>
<br>    
<a href="https://trello.com/b/2TH5CzmX/squad-marie-curie-womakers-code" target="_blank">
      <img height="48px" width="48px" alt="Icone Trello" src="https://cdn.icon-icons.com/icons2/3041/PNG/512/trello_logo_icon_189227.png">
</a>

<a href="https://drawsql.app/teams/squadmariecurrie/diagrams/books" target="_blank">
 <img height="48px" width="48px" alt="icone drawsql" src="https://pbs.twimg.com/profile_images/1016937460167684101/9wRBzBNZ_400x400.jpg">
</a>

<br>
<h3>Modelo de Banco de Dados:</h3>
<br>
O modelo de banco de dados pode ser encontrado no link a seguir e também no mermaid diagram abaixo

---

# Configurando o projeto 

1. No terminal de comando verifique:
 Instalação python: `python --version`
 Instalação `pip: pip --version`
 Se necessário atualize: `python -m pip install --upgrade pip` 

3. Criando e ativando ambiente virtual
    ```
   python -m venv .venv
    ```
    ```     
    ativa o venv: .\Scripts\activate
    ``` 

5. instalando django:  `pip install django` 
    Instalando djanjo paypal > `pip install django-paypal`
    Confirmar funcionamento : `python manage.py runserver`
    (devolve March 25, 2024 - 15:12:01
    Django version 5.0.3, using settings 'livraria.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.)

------------------------

## Requirements

- Para instalar todos as bibliotecas, use o requirements.txt

Entrar no seu ambiente virtual, e depois 
```
pip install -r requirements.txt
```

- Para atualizar os requirements

Entrar no ambiente virtual, e depois 
```
pip freeze > requirements.txt
```

> Evite enviar para o git o **pyvenv.cfg**, e as pastas **Lib** e **Scripts**
