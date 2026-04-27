import pytest
from urllib.parse import quote


@pytest.mark.asyncio
async def test_get_activities(client):
    # Arrange: `client` fixture

    # Act
    response = await client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Basketball" in data


@pytest.mark.asyncio
async def test_signup_and_unregister(client):
    # Arrange
    activity = "Chess Club"
    email = "tester@example.com"
    encoded = quote(activity)

    # Act: sign up
    signup_resp = await client.post(f"/activities/{encoded}/signup", params={"email": email})

    # Assert signup
    assert signup_resp.status_code == 200
    assert signup_resp.json()["message"] == f"Signed up {email} for {activity}"

    # Act: unregister
    unregister_resp = await client.delete(f"/activities/{encoded}/signup", params={"email": email})

    # Assert unregister
    assert unregister_resp.status_code == 200
    assert unregister_resp.json()["message"] == f"Unregistered {email} from {activity}"
