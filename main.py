from fastapi import FastAPI 
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
  return response.json()