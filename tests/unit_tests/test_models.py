def test_user_model():
    # Testa a criação de um usuário
    user = User(username='testuser', email='test@example.com', password='testpass')
    db.session.add(user)
    db.session.commit()

    assert user.id is not None
    assert User.query.filter_by(username='testuser').first() == user

def test_task_model():
    # Testa a criação de uma tarefa associada a um usuário
    user = User(username='testuser', email='test@example.com', password='testpass')
    db.session.add(user)
    db.session.commit()

    task = Task(
        title='Test Task',
        description='Test Description',
        due_date='2024-12-31',
        user_id=user.id
    )
    db.session.add(task)
    db.session.commit()

    assert task.id is not None
    assert user.tasks[0].title == 'Test Task'
