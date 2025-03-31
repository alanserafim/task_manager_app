def test_full_auth_flow(client):
    # Registra um novo usuário
    response = client.post('/register', data={
        'username': 'newuser',
        'email': 'new@example.com',
        'password': 'newpass123',
        'confirm_password': 'newpass123'
    }, follow_redirects=True)
    
    assert b'Account created' in response.data

    # Faz login com o usuário registrado
    response = client.post('/login', data={
        'email': 'new@example.com',
        'password': 'newpass123'
    }, follow_redirects=True)
    
    assert b'Dashboard' in response.data

    # Faz logout
    response = client.get('/logout', follow_redirects=True)
    assert b'Login' in response.data
