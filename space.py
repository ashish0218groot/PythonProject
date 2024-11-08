import requests

res = requests.get('http://api.open-notify.org/astros.json')
response = res.json()
print(response)
