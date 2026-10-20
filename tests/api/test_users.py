import pytest
from utils.validators import (assert_response_time, assert_user_structure, assert_users_list_structure, assert_empty_user_response, assert_carts_structure)
from data.users import ADD_USER, UPDATE_USER_PAYLOAD

pytestmark = pytest.mark.users

@pytest.mark.smoke
def test_get_all_users(api_client):
    response = api_client.users.get_all_users()

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert_users_list_structure(data)

@pytest.mark.smoke
def test_get_single_user(api_client):
    user_id = 1
    response = api_client.users.get_single_user(user_id)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data["id"] == user_id
    assert_user_structure(data)


def test_user_not_found(api_client):
    user_id = 5435
    response = api_client.users.get_single_user(user_id)

    assert response.status_code == 404
    assert_response_time(response)


def test_search_users(api_client):
    response = api_client.users.search_users(query="Daniel")

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert_users_list_structure(data)


def test_empty_users(api_client):
    response = api_client.users.search_users(query="Epifanio")

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert_empty_user_response(data)


def test_filter_users(api_client):
    key = "hair.color"
    value = 'Black'
    response = api_client.users.filter_users(key=key, value=value)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data['users'][0]['hair']['color'] == value
    assert_users_list_structure(data)


def test_empty_filter_users(api_client):
    key = "hair.color"
    value = 'vermelho'
    response = api_client.users.filter_users(key=key, value=value)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert_empty_user_response(data)


def test_limit_skip_users(api_client):
    limit = 2
    skip = 2
    select = 'firstName,email'
    response = api_client.users.limit_and_skip_users(limit=limit, skip=skip, select=select)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data['limit'] == limit
    assert data['skip'] == skip

    user = data['users'][0]

    assert "id" in user
    assert 'firstName' in user
    assert "email" in user

    assert isinstance(user['id'], int)
    assert isinstance(user['firstName'], str)
    assert isinstance(user['email'], str)


def test_sort_users(api_client):
    sortBy = 'lastName'
    order = 'asc'
    response = api_client.users.sort_users(sortBy=sortBy, order=order)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert_users_list_structure(data)


def test_users_carts_by_id(api_client):
    user_id = 1
    response = api_client.users.get_users_carts_by_id(user_id)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert_carts_structure(data)

    carts = data['carts'][0]
    assert carts['userId'] == user_id


def test_users_post_by_id(api_client):
    user_id = 1
    response = api_client.users.get_users_post_by_id(user_id)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert 'posts' in data
    assert isinstance(data['posts'], list)


def test_add_user(api_client):
    payload = (ADD_USER)
    response = api_client.users.add_new_user(payload)

    assert response.status_code == 201
    assert_response_time(response)

    data = response.json()

    assert_user_structure(data)


def test_patch_user(api_client):
    user_id = 1
    payload = {
        'lastName':'Arteaga'
    }
    response = api_client.users.patch_user(user_id,payload)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data['id'] == user_id
    assert data['lastName'] == payload['lastName']

    assert_user_structure(data)


def test_update_user(api_client):
    user_id = 1
    payload = (UPDATE_USER_PAYLOAD)
    response = api_client.users.put_user(user_id,payload)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data['id'] == user_id

    assert_user_structure(data)


def test_delete_user(api_client):
    user_id = 1
    response = api_client.users.delete_user(user_id)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data["id"] == user_id
    assert data["isDeleted"] is True