from datetime import timedelta

import pytest


@pytest.mark.get
@pytest.mark.no_rollback
@pytest.mark.happy_case
@pytest.mark.asyncio
async def test_update_user_happy_case(test_client, user_payload):
    """
    Create a random user > update user > get user > delete created user.
    """
    # creating at least one user
    post_response = test_client.post("user/create", json=user_payload)
    assert post_response.status_code == 201
    assert post_response.elapsed < timedelta(seconds=2.0)
    
    # update user
    patch_response = test_client.patch("user/{}".format(post_response.json().get('user_uuid')),
                                       json={"user_name": "test"},)
    assert patch_response.status_code == 202
    assert patch_response.elapsed < timedelta(seconds=2.0)
    
    # get user updated
    get_response = test_client.get("/user/{}".format(post_response.json().get('user_uuid')))
    assert get_response.status_code == 200
    assert isinstance(get_response.json(), dict)
    assert get_response.json().get('user_name') == 'test'
    assert get_response.elapsed < timedelta(seconds=2.0)

    # delete created user
    delete_response = test_client.delete("user/{}".format(post_response.json().get('user_uuid')))
    assert delete_response.status_code == 200
    assert delete_response.elapsed < timedelta(seconds=2.0)


@pytest.mark.get
@pytest.mark.no_rollback
@pytest.mark.sad_case
def test_update_invalid_user_sad_case(test_client):
    """
    Delete invalid user.
    """   
    patch_response = test_client.patch("/user/{}".format('invalid uuid'))
    assert patch_response.status_code == 422
    assert patch_response.json().get('detail')[0].get('type') == 'uuid_parsing'
    assert patch_response.elapsed < timedelta(seconds=2.0)