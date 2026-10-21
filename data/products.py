# --- IDs de productos ---
EXISTING_PRODUCT_ID = 5
EXISTING_PRODUCT_IDS = [1, 5, 10]
NON_EXISTENT_PRODUCT_ID = 545466541

# --- Búsquedas ---
SEARCH_QUERIES_WITH_RESULTS = ["samsung", "iphone", "laptop"]
SEARCH_QUERIES_WITHOUT_RESULTS = ["GTA VI", "zzzzz", "Dale Zelda, Dale"]

# --- Paginación ---
PRODUCT_SELECT = "title,price"
PAGINATION_CASES = [(2, 2), (5, 0), (1, 10)]   # (limit, skip)

# --- Ordenamiento ---
SORT_BY = "title"
SORT_ORDER = "desc"

# --- Categorías ---
EXISTING_CATEGORIES = ["smartphones", "laptops", "fragrances"]
NON_EXISTENT_CATEGORY = "Drogas"

# --- Payloads ---
SUCCESS_ADD_PRODUCT = {
        "title": "iPhone 16",
        "description": "the perfect balance of price and quality",
        "price": 800,
        "category": "smartphones",
    }

UPDATE_PRODUCT = {
        "title": "iPhone 16",
        "description": "the perfect balance of price and quality",
        "price": 800,
        "category": "smartphones",
    }

PATCH_PRODUCT = {
        "title": "iPhone 16",
}