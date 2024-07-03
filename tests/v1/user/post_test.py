from datetime import timedelta

import pytest


@pytest.mark.get
@pytest.mark.no_rollback
@pytest.mark.happy_case
@pytest.mark.asyncio
async def test_create_user_happy_case(test_client, user_payload):
    """
    Create a random user > delete created user.
    """
    # creating at least one user
    post_response = test_client.post("user/create", json=user_payload)
    assert post_response.status_code == 201
    assert post_response.elapsed < timedelta(seconds=2.0)
    
    # delete created user
    delete_response = test_client.delete("user/{}".format(post_response.json().get('user_uuid')))
    assert delete_response.status_code == 200
    assert delete_response.elapsed < timedelta(seconds=2.0)


@pytest.mark.get
@pytest.mark.no_rollback
@pytest.mark.sad_case
@pytest.mark.asyncio
async def test_create_user_sad_case(test_client):
    """
    Create a invalid user.
    """
    # creating a invalid user
    post_response = test_client.post("user/create", json={'invalid': 'error'})
    assert post_response.status_code == 422
    assert post_response.elapsed < timedelta(seconds=2.0)


