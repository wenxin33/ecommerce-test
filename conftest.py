import pytest

from api.base_client import BaseClient


@pytest.fixture
def client():
    """
    普通客户端，不带 token
    """
    return BaseClient()


@pytest.fixture
def token():
    """
    获取登录 token
    """
    client = BaseClient()

    response = client.post("/login", json={
        "username": "test001",
        "password": "123456"
    })

    data = response.json()

    assert data.get("code") == 200
    assert "token" in data

    return data["token"]


@pytest.fixture
def auth_client(token):
    """
    已登录客户端，自动携带 token
    """
    client = BaseClient()
    client.set_token(token)
    return client


@pytest.fixture
def reset_data():
    """
    每个需要清理状态的测试前后调用 reset
    """
    client = BaseClient()

    client.post("/reset")

    yield

    client.post("/reset")