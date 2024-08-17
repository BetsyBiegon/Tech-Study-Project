# tests/test_auth.py

import json

def test_register(test_client):
    response = test_client.post('/api/register', 
                                data=json.dumps({
                                    'username': 'testuser',
                                    'email': 'test@example.com',
                                    'password': 'password'
                                }),
                                content_type='application/json')
    assert response.status_code == 201

def test_login(test_client, new_user):
    test_client.post('/api/register', 
                     data=json.dumps({
                         'username': new_user.username,
                         'email': new_user.email,
                         'password': new_user.password
                     }),
                     content_type='application/json')
    
    response = test_client.post('/api/login', 
                                data=json.dumps({
                                    'email': new_user.email,
                                    'password': new_user.password
                                }),
                                content_type='application/json')
    
    assert response.status_code == 200
    assert 'access_token' in json.loads(response.data)
