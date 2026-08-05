from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@patch("app.api.users.load_users")
def test_get_users(mock_load_users):

    mock_load_users.return_value = []

    response = client.get("/users")

    assert response.status_code == 200

    assert response.json() == []