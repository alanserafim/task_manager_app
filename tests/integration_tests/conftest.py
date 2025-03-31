import pytest
from app import app, db
from models import User, Task

@pytest.fixture(scope='module')
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

@pytest.fixture
def test_user():
    user = User(username='testuser', email='test@example.com', password='testpass')
    db.session.add(user)
    db.session.commit()
    return user
