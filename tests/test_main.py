from fastapi.testclient import TestClient


def test_health(client: TestClient):
    """Test health check"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_read_main(client: TestClient):
    """Test main page"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"


def test_ico(client: TestClient):
    """Test ico"""
    response = client.get("/favicon.ico")
    assert response.status_code == 200
    assert (
        response.headers["Content-Type"] == "image/x-icon"
        or response.headers["Content-Type"] == "image/vnd.microsoft.icon"
    )


def test_tracks(client: TestClient):
    """Test tracks"""
    data = {"input_url": "https://example.com"}
    response = client.post("/tracks", data=data)
    assert response.status_code == 200
    assert response.json() is None
