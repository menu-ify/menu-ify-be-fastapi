from fastapi.testclient import TestClient
import vcr
import urllib3
from main import app 

client = TestClient(app)

@vcr.use_cassette('tests/fixtures/vcr_cassettes/unsplash_bacon.yaml', filter_query_parameters=['client_id'])
def test_read_main():
    response = client.get("/photos/bacon")
    assert response.status_code == 200

@vcr.use_cassette('tests/fixtures/vcr_cassettes/unsplash_bacon.yaml', filter_query_parameters=['client_id'])
def test_read_main_response():
    response = client.get("/photos/bacon")
    assert "results" in response.json()
