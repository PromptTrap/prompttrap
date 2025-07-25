def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_version(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json()["version"] == "0.1.0"
