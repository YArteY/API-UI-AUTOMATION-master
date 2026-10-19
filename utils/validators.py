from utils.config import MAX_RESPONSE_TIME_SECONDS

def assert_response_time(response,max_seconds=MAX_RESPONSE_TIME_SECONDS):
    assert response.elapsed.total_seconds() <= max_seconds

def assert_product_structure(product):

    assert "id" in product
    assert "title" in product
    assert "description" in product
    assert "price" in product
    assert "category" in product

    assert isinstance(product["id"], int)
    assert isinstance(product["title"], str)
    assert isinstance(product["description"], str)
    assert isinstance(product["price"], (int, float))
    assert isinstance(product["category"], str)

def assert_empty_response(data):
    assert "products" in data
    assert data["total"] == 0
    assert data["skip"] == 0
    assert data["limit"] == 0

def assert_product_list_structure(data):
    assert 'products' in data
    assert 'total' in data
    assert 'skip' in data
    assert 'limit' in data

    assert isinstance(data['products'], list)
    assert isinstance(data['total'], int)
    assert isinstance(data['skip'], int)
    assert isinstance(data['limit'], int)

    if data["products"]:
        assert_product_structure(data["products"][0])

def assert_category_structure(category):
    assert "slug" in category
    assert "name" in category
    assert "url" in category

    assert isinstance(category["slug"], str)
    assert isinstance(category["name"], str)
    assert isinstance(category["url"], str)


def assert_user_structure(data):
    assert "firstName" in data
    assert "lastName" in data
    assert 'maidenName' in data
    assert 'age' in data
    assert 'gender' in data
    assert 'email' in data
    assert 'phone' in data
    assert 'username' in data
    assert 'password' in data
    assert 'birthDate' in data
    assert 'image' in data

    assert isinstance(data['firstName'], str)
    assert isinstance(data['lastName'], str)
    assert isinstance(data['maidenName'], str)
    assert isinstance(data['age'], int)
    assert isinstance(data['gender'], str)
    assert isinstance(data['email'], str)
    assert isinstance(data['phone'], str)
    assert isinstance(data['username'], str)
    assert isinstance(data['password'], str)
    assert isinstance(data['birthDate'], str)
    assert isinstance(data['image'], str)


def assert_users_list_structure(data):
    assert 'users' in data
    assert 'total' in data
    assert 'skip' in data
    assert 'limit' in data

    assert isinstance(data['users'], list)
    assert isinstance(data['total'],int)
    assert isinstance(data['skip'],int)
    assert isinstance(data['limit'],int)
    if data["users"]:
        assert_user_structure(data["users"][0])


def assert_empty_user_response(data):
    assert "users" in data
    assert data["total"] == 0
    assert data["skip"] == 0
    assert data["limit"] == 0

def assert_carts_structure(data):
    assert 'carts' in data
    assert 'total' in data
    assert 'limit' in data
    assert 'skip' in data

    assert isinstance(data['carts'], list)
    assert isinstance(data['total'], int)
    assert isinstance(data['limit'], int)
    assert isinstance(data['skip'], int)

    carts = data['carts'][0]

    assert 'total' in carts
    assert 'discountedTotal' in carts
    assert 'userId' in carts
    assert 'totalProducts' in carts
    assert 'totalQuantity' in carts

    assert isinstance(carts['total'], float)
    assert isinstance(carts['discountedTotal'], float)
    assert isinstance(carts['userId'], int)
    assert isinstance(carts['totalProducts'], int)
    assert isinstance(carts['totalQuantity'], int)