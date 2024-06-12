import requests

# Initialize the PocketBase API URL
base_url = 'http://138.2.78.67:8090/api'

# Admin login credentials
admin_email = 'jangidvedant01@gmail.com'
admin_password = 'smfLfNQhMaNCih7'

# Function to log in as admin and get the authorization token
def admin_login(email, password):
    url = f"{base_url}/admins/auth-with-password"
    payload = {
        "identity": email,
        "password": password
    }
    response = requests.post(url, json=payload)
    response_data = response.json()
    if response.status_code == 200:
        return response_data['token']
    else:
        print('Error:', response_data)
        return None

# Function to fetch a paginated records list with a valid filter
def fetch_paginated_records(token, page, per_page, filter_str):
    url = f"{base_url}/collections/users/records"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'page': page,
        'perPage': per_page,
        'filter': filter_str
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# Function to fetch all records with sorting
def fetch_all_records(token):
    url = f"{base_url}/collections/users/records"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'sort': '-created',
        'perPage': 500  # Adjust the limit as necessary
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# Function to fetch the first record that matches a specified filter
def fetch_first_record(token, filter_str, expand_fields):
    url = f"{base_url}/collections/users/records"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'filter': filter_str,
        'expand': expand_fields,
        'perPage': 1
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# Authenticate and get the token
token = admin_login(admin_email, admin_password)
if token:
    # Fetch all records
    all_records = fetch_all_records(token)
    print('All Records:', all_records)

    # Print each user record
    if 'items' in all_records:
        for user in all_records['items']:
            print(user)
