from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hola, mundo"}


def test_create_and_read_item():
    response = client.post("/items/1", json={"name": "Libro", "price": 9.99})
    assert response.status_code == 201

    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Libro", "price": 9.99}


def test_read_missing_item():
    response = client.get("/items/999")
    assert response.status_code == 404
