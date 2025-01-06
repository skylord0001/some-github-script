import requests

api_token = ""
headers = {"Authorization": f"Bearer {api_token}"}

url = "https://api.github.com/rate_limit"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
