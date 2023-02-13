from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
import requests 
from dotenv import load_dotenv 
import os
import json

def configure():
  load_dotenv() 


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


