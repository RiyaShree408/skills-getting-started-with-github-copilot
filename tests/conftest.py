import pytest
from httpx import AsyncClient
from src.app import app


@pytest.fixture
async def client():
    """Async test client for the ASGI app.

    Provides an `httpx.AsyncClient` configured to send requests directly to
    the `app` from `src.app`.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
