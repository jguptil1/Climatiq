import requests
api_url = "https://api.example.com/climatiq"
api_key = 'ZM85KK6A7M4CG1NA7PJYP6KZVDE9'
# response = requests.get('https://beta4.api.climatiq.io')
# print(response.status_code)

def get_climatiq_data(location):
    headers = {
        "Authorization": f"Bearer {api_key}" if api_key else None,
        # Add any additional headers required by the API
    }

    params = {
        "location": location,
        # Add any other query parameters needed by the API
    }

    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

location = "New York"  # Replace this with your desired location
data = get_climatiq_data(location)

if data:
    # Process the data as per the API response format
    print(data)