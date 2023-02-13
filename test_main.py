from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

def test_main(keyword = "cheese"): 
  response = client.get("/photos/{keyword}")
  assert response.status_code == 200 