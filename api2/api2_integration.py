import os
import requests

def get_data_from_api2():
    api_key = os.getenv('API_KEY')
    response = requests.get('ACTUAL_API_2_ENDPOINT', headers={'Authorization': f'Bearer {api_key}'})
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == "__main__":
    data = get_data_from_api2()
    print(data)
