import requests

url = 'https://last-airbender-api.fly.dev/api/v1/characters'

response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    print(json_data)

else: 
    print(f"Error: {response.status_code}")