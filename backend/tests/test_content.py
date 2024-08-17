# tests/test_content.py

import json

def test_create_content(test_client, new_user):
    # First, register and log in the user
    test_client.post('/api/register', 
                     data=json.dumps({
                         'username': new_user.username,
                         'email': new_user.email,
                         'password': new_user.password
                     }),
                     content_type='application/json')
    
    login_response = test_client.post('/api/login', 
                                      data=json.dumps({
                                          'email': new_user.email,
                                          'password': new_user.password
                                      }),
                                      content_type='application/json')
    
    access_token = json.loads(login_response.data)['access_token']

    # Create content
    response = test_client.post('/api/content', 
                                data=json.dumps({
                                    'title': 'Test Content',
                                    'body': 'This is a test content.',
                                    'category': 'Fullstack'
                                }),
                                headers={'Authorization': f'Bearer {access_token}'},
                                content_type='application/json')
    
    assert response.status_code == 201
    assert 'Test Content' in str(response.data)

def test_get_content(test_client):
    response = test_client.get('/api/content')
    assert response.status_code == 200
    assert len(json.loads(response.data)) > 0
