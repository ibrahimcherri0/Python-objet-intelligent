import requests
url = "https://systeme-domotique-default-rtdb.europe-west1.firebasedatabase.app/test.json"
payload = '{"words":false}'
header = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.request("PUT",url, data=payload)
print(response.text)