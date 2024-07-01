import requests
 
endpoint = "http://api.open-notify.org/iss-now.json"
 
response = requests.get(url=endpoint)
 
response.raise_for_status() # development mode
 
if response.status_code == 200: # production mode
    data = response.json()['iss_position']
    print(f"Latitude: {data['latitude']} Longitude: {data['longitude']}")
else:
    print("\nErro: não foi possível aceder ao endpoint indicado!\n")
    

# python -m venv env
# env\Scripts\activate
# criar requirements.txt
# pip install -r requirements.txt