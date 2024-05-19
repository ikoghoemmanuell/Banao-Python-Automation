import requests

response = requests.get('https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=a5843d7ee58ccb997497414f3715c46e&user_id=200666009%40N05&format=json&nojsoncallback=1')

response_json = response.json()

# validate the response
if response_json.get('stat') != 'ok':
    print("API call failed with status:", response_json.get('stat'), "& status code:", response.status_code)
else:
    print("API call successful with status:", response_json.get('stat'), "& status code:", response.status_code)
