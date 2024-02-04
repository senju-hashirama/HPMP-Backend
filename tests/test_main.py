from starlette.testclient import TestClient
import pytest
from backend.main import app

token=None

client = TestClient(app)
@pytest.fixture
def token():
    print("Setting up Authorization token")
    response=client.post("/login",json={"email":"test@gmail.com","password":"pass123"})
    token=response.json()["token"]
    return token

    
def test_login():
    response=client.post("/login",json={"email":"test@gmail.com","password":"pass123"})
    assert response.status_code== 200
    assert response.json()["status"]=="ok"

def test_search(token):
    response=client.get("/search/Maharani",headers={"Authorization":token})
    print(response.json())
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_get_playlists(token):
    response=client.get("/get_playlists",headers={"Authorization":token})
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_recently_played(token):
    response=client.get("/recently_played",headers={"Authorization":token})
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_get_song(token):
    response=client.get("/song/ZpVOC8H0",headers={"Authorization":token})
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_get_playlist_info(token):
    response=client.get("/playlist_info/65b616470be8c5726d6351ea",headers={"Authorization":token})

    assert response.status_code == 200
    assert response.json()["status"] == "ok"



    

