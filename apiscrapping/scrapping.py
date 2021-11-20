import requests

import tools

api_user = 'http://localhost:5852/api/user'
api_product = 'http://localhost:5853/api/product/all'

def users_all():
    try:    
        response = requests.get(api_user)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        print('Error: url not exists!!')
        return None

def products_all():
    try:
        response = requests.get(api_product)
        if response and response.status_code == 200:
            return response.json()
        return None
    except:
        print('Error: url not exists!!')
        return None

def main():
    users = users_all()
    products = products_all()
    
    if users:
        tools.start_create_file('users', users, 'usr')
    
    if products:
        tools.start_create_file('products', products, 'prod')


if __name__ == "__main__":
    main()