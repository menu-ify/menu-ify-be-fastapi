from fastapi import FastAPI
from fastapi.testclient import TestClient
import pandas as pd 
import requests 
from dotenv import load_dotenv 
import os

def configure():
  load_dotenv() 


app = FastAPI()

@app.get("/photos/{keyword}")
def get_photos(keyword: str):
  configure()
  url = f"https://api.unsplash.com/search/photos?page=1&query=" + keyword + "&client_id=" + os.getenv("api_key")
  response = requests.get(url)
  new = response.json()
  new_results = new["results"]
  photo_array = []
  for item in new_results:
    photo_array.append((item["urls"]["raw"]))
  return {"results": photo_array }

client = TestClient(app)

def test_read_main():
    response = client.get("/photos/bacon")
    assert response.status_code == 200

def test_read_main_response():
    response = client.get("/photos/bacon")
    assert "results" in response.json()
