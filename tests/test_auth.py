from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient
from core.auth import get_token
from core.config import PROMPTTRAP_API_KEYS

app = FastAPI()

@app.get("/")
def read_root(token: str = Depends(get_token)):
    return {"token": token}

client = TestClient(app)

def test_get_token_valid():
    PROMPTTRAP_API_KEYS.append("test_key")
    response = client.get("/", headers={"Authorization": "Bearer test_key"})
    assert response.status_code == 200
    assert response.json() == {"token": "test_key"}

def test_get_token_missing():
    response = client.get("/")
    assert response.status_code == 401
    assert response.json() == {"detail": "Missing authorization header"}

def test_get_token_invalid_type():
    response = client.get("/", headers={"Authorization": "Invalid test_key"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid token type"}

def test_get_token_invalid_token():
    response = client.get("/", headers={"Authorization": "Bearer invalid_key"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid token"}