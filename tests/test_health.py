from fastapi.testclient import TestClient
from src.core.app import create_app

app = create_app()
client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}
