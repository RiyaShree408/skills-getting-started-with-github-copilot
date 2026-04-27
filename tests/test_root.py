def test_root_redirect(client):
    # Arrange: `client` fixture provided by tests/conftest.py

    # Act
    response = client.get("/")

    # Assert
    # The root endpoint issues a redirect to `/static/index.html`.
    assert response.status_code == 307
    assert response.headers.get("location") == "/static/index.html"
