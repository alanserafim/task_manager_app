def test_home_redirect(test_client):
    # Testa se a rota '/' redireciona para login quando não autenticado
    response = test_client.get('/')
    assert response.status_code == 302
    assert '/login' in response.location

def test_user_registration(test_client):
    # Testa o registro de um novo usuário
    response = test_client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123',
        'confirm_password': 'testpass123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Account created' in response.data

def test_task_creation(test_client):
    # Cria um usuário de teste
    user = User(username='testuser', email='test@example.com', password='testpass')
    db.session.add(user)
    db.session.commit()

    # Login simulado (usando sessão)
    with test_client.session_transaction() as session:
        session['user_id'] = user.id

    # Testa a criação de uma tarefa
    response = test_client.post('/add_task', data={
        'title': 'Test Task',
        'description': 'Test Description',
        'due_date': '2024-12-31'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Test Task' in response.data
