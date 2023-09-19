import requests
import json

# We can use this to see if we're running afoul of the API limits on GitHub

url = "https://api.github.com/rate_limit"
headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
print(json.dumps(response.json(), indent=4))
