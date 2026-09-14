from fastapi import FastAPI, Query
import requests

app = FastAPI()


@app.get('/api/hello')
def hello_world():
    return {'Hello': 'World'}


@app.get('/api/restaurants/')
def get_restaurants(restaurant: str = Query(None)):
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        if restaurant is None:
            return {'data': json_data}

        restaurant_data = []
        for item in json_data:
            if item['Company'] == restaurant:
                restaurant_data.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurant': restaurant, 'Menu': restaurant_data}
    else:
        print(f'O erro foi {response.status_code} - {response.text}')
