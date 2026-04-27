import pytest
from httpx import Client
from src.app import app


@pytest.fixture
def client():
    """Synchronous test client for the ASGI app.

    Uses `httpx.Client` so tests can remain synchronous and not require
    `pytest-asyncio`.
    """
    with Client(app=app, base_url="http://test") as c:
        yield c
