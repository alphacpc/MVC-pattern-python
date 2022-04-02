import requests

api_url = 'https://jsonplaceholder.typicode.com/'

def fetch_all(endpoint):

    response = requests.get(api_url + endpoint)
    
    if response.status_code == 200:
        
        return response.json()

    else:
        return None