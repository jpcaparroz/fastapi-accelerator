from datetime import timedelta

import pytest


@pytest.mark.get
@pytest.mark.no_rollback
@pytest.mark.happy_case
@pytest.mark.asyncio
async def test_get_all_users_with_one_user_happy_case(test_client, user_payload):
    """
    Create a random user > search for least one user endpoint > delete created user.
    """
    # creating at least one user
    post_response = test_client.post("user/create", json=user_payload)
    assert post_response.status_code == 201

    # fetching all users   
    get_response = test_client.get("/user/")
    assert get_response.status_code == 200
    assert isinstance(get_response.json(), list)
    assert get_response.elapsed < timedelta(seconds=2.0)

    # delete created user
    delete_response = test_client.delete("user/{}".format(post_response.json().get('user_uuid')))
    assert delete_response.status_code == 200
    assert delete_response.elapsed < timedelta(seconds=2.0)


@pytest.mark.get
@pytest.mark.no_rollback
@pytest.mark.happy_case
def test_get_user_happy_case(test_client, user_payload):
    """
    Create a random user > search for user endpoint > delete created user.
    """
    # creating at least one user
    post_response = test_client.post("user/create", json=user_payload)
    assert post_response.status_code == 201

    # fetching user   
    get_response = test_client.get("/user/{}".format(post_response.json().get('user_uuid')))
    assert get_response.status_code == 200
    assert isinstance(get_response.json(), dict)
    assert get_response.json().get('user_uuid') == post_response.json().get('user_uuid')
    assert get_response.elapsed < timedelta(seconds=2.0)

    # delete created user
    delete_response = test_client.delete("user/{}".format(post_response.json().get('user_uuid')))
    assert delete_response.status_code == 200
    assert delete_response.elapsed < timedelta(seconds=2.0)


@pytest.mark.get
@pytest.mark.no_rollback
@pytest.mark.sad_case
def test_get_non_exist_user_sad_case(test_client, get_id):
    """
    Get non exists user.
    """ 
    get_response = test_client.get("/user/{}".format(get_id))
    assert get_response.status_code == 404
    assert get_response.elapsed < timedelta(seconds=2.0)


@pytest.mark.get
@pytest.mark.no_rollback
@pytest.mark.sad_case
def test_get_invalid_user_sad_case(test_client):
    """
    Get invalid user.
    """   
    get_response = test_client.get("/user/{}".format('invalid uuid'))
    assert get_response.status_code == 422
    assert get_response.json().get('detail')[0].get('type') == 'uuid_parsing'
    assert get_response.elapsed < timedelta(seconds=2.0)