def test_full_task_lifecycle(client, test_user):
    # Login (simula sessão)
    with client.session_transaction() as session:
        session['user_id'] = test_user.id

    # Cria uma nova tarefa
    response = client.post('/add_task', data={
        'title': 'Integration Task',
        'description': 'Test Description',
        'due_date': '2024-12-31'
    }, follow_redirects=True)
    
    assert b'Integration Task' in response.data

    # Edita a tarefa
    task = Task.query.filter_by(title='Integration Task').first()
    response = client.post(f'/edit_task/{task.id}', data={
        'title': 'Updated Task',
        'description': 'Updated Description',
        'due_date': '2025-01-01',
        'status': 'Completed'
    }, follow_redirects=True)
    
    assert b'Updated Task' in response.data

    # Exclui a tarefa
    response = client.get(f'/delete_task/{task.id}', follow_redirects=True)
    assert b'Updated Task' not in response.data
