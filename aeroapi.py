import requests
import os

apiKey = os.getenv('AEROAPI_KEY')
apiUrl = "https://aeroapi.flightaware.com/aeroapi/"

tail = 'N231ER'
payload = {'max_pages': 1}
auth_header = {'x-apikey':apiKey}

response = requests.get(apiUrl + f"/flights/{tail}",
    params=payload, headers=auth_header)

print(f"Locating {tail} ...")
if response.status_code == 200:
    airport = response.json().get('flights')[0].get('destination').get('code')
    print(f"{tail} is in {airport}")
else:
    print("Error executing request")
    print(response.json())
