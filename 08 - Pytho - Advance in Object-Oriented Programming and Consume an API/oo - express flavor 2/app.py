import requests

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    restaurant_data = {}
    for item in json_data:
        restaurant_name = item['Company']
        if restaurant_name not in restaurant_data:
            restaurant_data[restaurant_name] = []
        restaurant_data[restaurant_name].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
else:
    print(f'O erro foi {response.status_code}')

print(restaurant_data['McDonald’s'])