import pytest
from utils.validators import (assert_response_time, assert_product_list_structure, assert_product_structure,
                   assert_category_structure, assert_empty_response)

pytestmark = pytest.mark.products

@pytest.mark.smoke
def test_get_all_products(api_client):
    response = api_client.products.get_all_products()

    assert response.status_code == 200
    assert_response_time(response)
    assert_product_list_structure(response.json())

@pytest.mark.smoke
def test_get_single_product(api_client):
    product_id= 5
    response = api_client.products.get_single_product(product_id)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data["id"] == product_id
    assert_product_structure(data)


def test_fail_get_single_product(api_client):
    product_id= 545466541
    response = api_client.products.get_single_product(product_id)

    assert response.status_code == 404
    assert_response_time(response)


def test_success_search_products(api_client):
    response = api_client.products.search_products(query="samsung")

    assert response.status_code == 200
    assert_response_time(response)

    assert_product_list_structure(response.json())


def test_empty_search_products(api_client):
    response = api_client.products.search_products(query="GTA VI")
    data = response.json()

    assert response.status_code == 200
    assert_response_time(response)
    assert_empty_response(data)


def test_limit_and_skip_product(api_client):
    limit = 2
    skip = 2
    select = "title,price"
    response = api_client.products.limit_and_skip_product(limit=limit, skip=skip, select=select)
    data = response.json()

    assert response.status_code == 200
    assert_response_time(response)

    assert data["limit"] == limit
    assert data["skip"] == skip


def test_filter_products(api_client):
    sortBy = "title"
    order = "desc"
    response = api_client.products.sort_products(sortBy=sortBy, order=order)
    data = response.json()

    assert response.status_code == 200
    assert_response_time(response)

    assert_product_list_structure(data)

@pytest.mark.smoke
def test_get_all_categories(api_client):
    response = api_client.products.get_all_categories()
    data = response.json()

    assert response.status_code == 200
    assert_response_time(response)
    assert_category_structure(data[0])


def test_get_categories_list(api_client):
    response = api_client.products.get_categories_list()

    assert response.status_code == 200
    assert_response_time(response)


def test_get_category_name(api_client):
    category_name = "smartphones"
    response = api_client.products.get_category_name(category_name)

    assert response.status_code == 200
    assert_response_time(response)
    assert_product_list_structure(response.json())


def test_fail_get_category_name(api_client):
    category_name = "Drogas"
    response = api_client.products.get_category_name(category_name)

    assert response.status_code == 200
    assert_response_time(response)
    assert_empty_response(response.json())

@pytest.mark.smoke
def test_success_add_product(api_client):
    payload = {
        "title": "iPhone 16",
        "description": "the perfect balance of price and quality",
        "price": 800,
        "category": "smartphones",
    }
    response = api_client.products.add_product(payload)

    assert response.status_code == 201
    assert_response_time(response)

    assert_product_structure(response.json())


def test_update_product(api_client):
    product_id= 5
    payload = {
        "title": "iPhone 16",
        "description": "the perfect balance of price and quality",
        "price": 800,
        "category": "smartphones",
    }
    response = api_client.products.update_product(product_id, payload)

    assert response.status_code == 200
    assert_response_time(response)
    data = response.json()

    assert data["id"] == product_id
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["price"] == payload["price"]
    assert data["category"] == payload["category"]
    assert_product_structure(data)


def test_patch_product(api_client):
    product_id= 5
    payload = {
        "title": "iPhone 16",
    }
    response = api_client.products.patch_product(product_id, payload)

    assert response.status_code == 200
    assert_response_time(response)
    data = response.json()

    assert data["id"] == product_id
    assert data["title"] == payload["title"]

@pytest.mark.smoke
def test_delete_product(api_client):
    product_id= 5
    response = api_client.products.delete_product(product_id)

    assert response.status_code == 200
    assert_response_time(response)
    data = response.json()

    assert data["id"] == product_id
    assert data["isDeleted"] is True

