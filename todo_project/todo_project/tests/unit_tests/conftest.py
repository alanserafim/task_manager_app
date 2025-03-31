import pytest
from flask import Flask
from todo_project import app, db
from models import User, Task

@pytest.fixture(scope='module')
def test_client():
    # Configuração do app para testes
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False  # Desativa CSRF para formulários

    # Cria banco de dados em memória
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            yield testing_client
            db.drop_all()
