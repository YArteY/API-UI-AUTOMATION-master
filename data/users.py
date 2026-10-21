EXISTING_USER_ID = 1
NON_EXISTENT_USER_ID = 5435
USER_SEARCH_QUERIES_WITH_RESULTS = ["Daniel", "John", "Emily"]
USER_SEARCH_QUERIES_WITHOUT_RESULTS = ["Epifanio", "Maricarmen","Teodocia"]
USER_FILTER_KEY = "hair.color"
USER_FILTER_VALID_VALUES = ["Black","White","Blonde"]
USER_FILTER_INVALID_VALUES = ["Vermelho","Vomito","Ceniza"]
USER_LIMIT = 2
USER_SKIP = 2
USER_SELECT = "firstName,email"
PATCH_USER_PAYLOAD = {"lastName": "Arteaga"}

#------Payloads
VALID_USER = {
     'username': 'emilys',
     'password': 'emilyspass',
     'expiresInMins': 30
 }

INVALID_USER = {
    'username': 'daniel',
    'password': 'danielpass',
    'expiresInMins': 30
}

ADD_USER = {
    'firstName': 'Muhammad',
    'lastName': 'Ovi',
    'age': 250,
    'maidenName': 'Alibaba',
    'gender': 'male',
    'email': 'muhamadd@sapoperro.com',
    'username': 'Muahammad',
    'password': 'Muhamadpass'
}

UPDATE_USER_PAYLOAD = {
    "firstName": "John",
    "lastName": "Smith",
    "email": "john.smith@example.com",
}

UI_USER = {
    'username': 'standard_user',
    'password': 'secret_sauce',
}