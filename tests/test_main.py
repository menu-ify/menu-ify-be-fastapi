from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

def test_read_main_response():
    response = client.get("/photos/bacon")
    photo_list = response.json()["results"]
    assert response.status_code == 200
    assert "results" in response.json()
    assert len(photo_list) == 10

def test_read_no_photos_found():
    response = client.get("/photos/asdfjklqweruiop")
    assert response.status_code == 200
    assert response.json() == {"message": "No photos found"}

def test_read_blank_query_param():
    response = client.get("/photos/ ")
    assert response.status_code == 200
    assert response.json() == {"message": "No photos found"}