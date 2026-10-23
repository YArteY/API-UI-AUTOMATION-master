import pytest

from data.products import UPDATE_PRODUCT, PATCH_PRODUCT, SUCCESS_ADD_PRODUCT, EXISTING_PRODUCT_ID, \
    NON_EXISTENT_PRODUCT_ID, SEARCH_QUERIES_WITH_RESULTS, SEARCH_QUERIES_WITHOUT_RESULTS, SORT_BY, SORT_ORDER, \
    EXISTING_CATEGORIES, NON_EXISTENT_CATEGORY, EXISTING_PRODUCT_IDS, PAGINATION_CASES, PRODUCT_SELECT, \
    NEGATIVE_PAGINATION_CASES
from utils.validators import (assert_response_time, assert_product_list_structure, assert_product_structure,
                   assert_category_structure, assert_empty_response)

pytestmark = pytest.mark.products

@pytest.mark.smoke
def test_get_all_products(api_client):
    response = api_client.products.get_all_products()

    assert response.status_code == 200
    assert_response_time(response)
    assert_product_list_structure(response.json())

@pytest.mark.parametrize("product_id",EXISTING_PRODUCT_IDS)
def test_get_product_by_id(api_client,product_id):
    response = api_client.products.get_single_product(product_id)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data["id"] == product_id, (
        f"Expected product ID {product_id}, "
        f"but received {data.get('id')}"
    )
    assert_product_structure(data)

@pytest.mark.parametrize("product_id",NON_EXISTENT_PRODUCT_ID)
def test_get_product_by_id_not_found(api_client,product_id):
    response = api_client.products.get_single_product(product_id)

    assert response.status_code == 404
    assert_response_time(response)

@pytest.mark.parametrize("query",SEARCH_QUERIES_WITH_RESULTS)
def test_success_search_products(api_client,query):
    response = api_client.products.search_products(query=query)

    assert response.status_code == 200
    assert_response_time(response)

    assert_product_list_structure(response.json())

@pytest.mark.parametrize("query",SEARCH_QUERIES_WITHOUT_RESULTS)
def test_empty_search_products(api_client, query):
    response = api_client.products.search_products(query=query)
    data = response.json()

    assert response.status_code == 200
    assert_response_time(response)
    assert_empty_response(data)

@pytest.mark.parametrize("limit,skip",PAGINATION_CASES)
def test_limit_and_skip_product(api_client, limit, skip):
    response = api_client.products.limit_and_skip_product(limit=limit, skip=skip, select=PRODUCT_SELECT)
    data = response.json()

    assert response.status_code == 200
    assert_response_time(response)

    assert data["limit"] == limit
    assert data["skip"] == skip

@pytest.mark.parametrize("limit,skip", NEGATIVE_PAGINATION_CASES)
def test_negative_limit_and_skip_product(api_client,limit,skip):
    response = api_client.products.limit_and_skip_product(limit=limit, skip=skip, select=PRODUCT_SELECT)

    assert response.status_code == 400
    assert_response_time(response)


def test_sort_products(api_client):
    sortBy = SORT_BY
    order = SORT_ORDER
    response = api_client.products.sort_products(sortBy=sortBy, order=order)
    data = response.json()

    assert response.status_code == 200
    assert_response_time(response)

    assert_product_list_structure(data)


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

@pytest.mark.parametrize("category_name",EXISTING_CATEGORIES)
def test_get_category_name(api_client,category_name):
    response = api_client.products.get_category_name(category_name)

    assert response.status_code == 200
    assert_response_time(response)
    assert_product_list_structure(response.json())

@pytest.mark.parametrize("category_name",NON_EXISTENT_CATEGORY)
def test_fail_get_category_name(api_client,category_name):
    response = api_client.products.get_category_name(category_name)

    assert response.status_code == 200
    assert_response_time(response)
    assert_empty_response(response.json())


def test_success_add_product(api_client):
    payload = SUCCESS_ADD_PRODUCT
    response = api_client.products.add_product(payload)

    assert response.status_code == 201
    assert_response_time(response)

    assert_product_structure(response.json())


def test_update_product(api_client):
    product_id= EXISTING_PRODUCT_ID
    payload = UPDATE_PRODUCT
    response = api_client.products.update_product(product_id, payload)

    assert response.status_code == 200
    assert_response_time(response)
    data = response.json()

    assert data["id"] == product_id, (
        f"Expected product ID {product_id}, "
        f"but received {data.get('id')}"
    )
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["price"] == payload["price"]
    assert data["category"] == payload["category"]
    assert_product_structure(data)


def test_patch_product(api_client):
    product_id= EXISTING_PRODUCT_ID
    payload = PATCH_PRODUCT
    response = api_client.products.patch_product(product_id, payload)

    assert response.status_code == 200
    assert_response_time(response)
    data = response.json()

    assert data["id"] == product_id, (
        f"Expected product ID {product_id}, "
        f"but received {data.get('id')}"
    )
    assert data["title"] == payload["title"]


def test_delete_product(api_client):
    product_id= EXISTING_PRODUCT_ID
    response = api_client.products.delete_product(product_id)

    assert response.status_code == 200
    assert_response_time(response)
    data = response.json()

    assert data["id"] == product_id, (
        f"Expected product ID {product_id}, "
        f"but received {data.get('id')}"
    )
    assert data["isDeleted"] is True

