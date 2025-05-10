import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_endpoint(client):
    response = client.post('/add', json={'a': 2, 'b': 3})
    assert response.status_code == 200
    assert response.json['result'] == 5

def test_divide_endpoint_zero(client):
    response = client.post('/divide', json={'a': 5, 'b': 0})
    assert response.status_code == 400
    assert "Cannot divide by zero" in response.json['error']