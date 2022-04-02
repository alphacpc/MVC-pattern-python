import requests
from Config.connectDB import Database


api_url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(api_url)
    
if response.status_code == 200:

    print(response.content.decode('utf-8'))
    u = Database()
    cursor = u.connexion()
else:
    print("bakhoul")