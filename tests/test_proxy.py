import respx
from httpx import Response


def test_proxy_openai(client):
    with respx.mock:
        respx.post("https://api.openai.com/v1/completions").mock(return_value=Response(200, json={"foo": "bar"}))
        response = client.post("/api/openai/completions", json={"prompt": "test"}, headers={"Authorization": "Bearer key1"})
        assert response.status_code == 200
        assert response.json() == {"foo": "bar"}

def test_proxy_claude(client):
    with respx.mock:
        respx.post("https://api.anthropic.com/v1/messages").mock(return_value=Response(200, json={"foo": "bar"}))
        response = client.post("/api/claude/v1/messages", json={"prompt": "test"}, headers={"Authorization": "Bearer key1"})
        assert response.status_code == 200
        assert response.json() == {"foo": "bar"}

def test_proxy_azure(client):
    with respx.mock:
        respx.post("https://your-resource.openai.azure.com/completions").mock(return_value=Response(200, json={"foo": "bar"}))
        response = client.post("/api/azure/completions", json={"prompt": "test"}, headers={"Authorization": "Bearer key1"})
        assert response.status_code == 200
        assert response.json() == {"foo": "bar"}
