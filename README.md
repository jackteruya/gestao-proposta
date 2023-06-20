# Gestao Emprestimo

Para ambiente linux.

Com do docker instaldo, caso não tenha -> https://docs.docker.com/engine/install/ e https://docs.docker.com/compose/install/


Para rodar a aplicação, no docker-compose.yml para subir um container, no terminal.

    $ docker-compose build
    $ docker-compose up



Ou caso não tenha o docker instalado, mas será necessario ter o python instalado, de preferencia a versão 3.11:
    
    1-Craindo o ambiente:
        $ python -m venv .venv

    2-Ativando o ambiente no linux:
        $ source .venv/bin/activate

    3-Instalando os requisitos:
        $ pip install -r requierements.txt

    4-Rodar a aplicação django, (sera http://127.0.0.1:8000/)
        $ python manage.py runserver

    5-Celery:
        $ celery -A gestao_emprestimo worker --loglevel=INFO
    
    6-Usuario ADMIN -> http://localhost:8000/admin:
        username: admin
        password: 123456

obs.: Será necessario ter o RabbitMQ instalado localmente na porta 5672, password pass123 e user admin