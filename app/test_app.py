from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_metrics_counts_requests():
    client = app.test_client()
    client.get("/")
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"app_requests_total" in response.data
