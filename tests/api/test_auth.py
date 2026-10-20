import pytest
from data.users import VALID_USER, INVALID_USER
from utils.validators import assert_response_time

pytestmark = pytest.mark.auth

@pytest.mark.smoke
def test_success_login(api_client):
    response = api_client.auth.login(VALID_USER)
    data = response.json()

    assert response.status_code == 200
    assert data['username'] == VALID_USER['username']
    assert 'accessToken' in data
    assert data['accessToken']
    assert_response_time(response)

@pytest.mark.smoke
def test_logout(authenticated_user):
    authenticated_user.auth.logout()
    assert 'Authorization' not in authenticated_user.session.headers

@pytest.mark.smoke
def test_failure_login(api_client):
    response = api_client.auth.login(INVALID_USER)
    data = response.json()

    assert response.status_code == 400
    assert 'accessToken' not in data
    assert_response_time(response)

@pytest.mark.smoke
def test_current_user(authenticated_user):
    response = authenticated_user.auth.current_user()

    assert response.status_code == 200
    assert_response_time(response)