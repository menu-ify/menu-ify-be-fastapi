from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

def test_read_main():
    response = client.get("/photos/bacon")
    assert response.status_code == 200

def test_read_main_response():
    response = client.get("/photos/bacon")
    assert "results" in response.json()

def test_no_photos_found():
    response = client.get("/photos/asdfjklqweruiop")
    assert "message" in response.json()