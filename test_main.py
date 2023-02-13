from fastapi.testclient import TestClient 
from dotenv import load_dotenv 
import os

from main import app  

def configure():
  load_dotenv() 

client = TestClient(app)


def test_main(keyword = 'cheese'): 
  configure()
  response = client.get("/photos/{keyword}")
  assert response.status_code == 200 