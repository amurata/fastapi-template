from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings


def test_get_users_me(client: TestClient, db: Session, auth_headers):
    # print(auth_headers)
    response = client.get("users/me", headers=auth_headers)
    data = response.json()
    print(data)

    assert data["email"] == settings.TEST_USER_EMAIL
