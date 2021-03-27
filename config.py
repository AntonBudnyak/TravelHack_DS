import os

API_KEY_NAME_IN_QUERY = 'access_token'
API_KEY_NAME_IN_HEADER = 'Authorization'
API_KEY = os.getenv('API_KEY')

# Personal recommendations
top_k = 50
