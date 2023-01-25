import requests

url = 'https://systeme-domotique-default-rtdb.europe-west1.firebasedatabase.app/test.json'

resp = requests.get(url=url)
data = resp.json() # Check the JSON Response Content documentation below
print(data)