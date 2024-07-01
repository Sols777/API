import requests
import beaupy


endpoint = "https://dummyjson.com/products"

parameters = {
    'sortBy' : 'price',
    # 'limit' : 20 ,
    'order' : 'desc',
    'select' : 'title,price,reviews,category'
}

# id title price rating

response = requests.get(url = endpoint , params = parameters)
listProducts = response.json()['products']


# for product in listProducts:
#     print(product)
#     print(f'link: https://dummyjson.com/products/{product["id"]}')
#     print('*' * 100)

reviewsList = []

for prod in listProducts:
    reviewsList.append(f"Produto: {prod['title']}\n")

    
def getItemID():
    op = int(beaupy.select(reviewsList, cursor="->", cursor_style='green', return_index=True))
    return op

def menu():
    id = getItemID()
    selected = listProducts[id]['reviews']
    for prod in selected:
        print(f"comment: {prod['comment']} from {prod['reviewerName']}")
    # print(selected['reviews'])
        
#
# menu()

def listCategories():
    endpoint = 'https://dummyjson.com/products/categories'
    response = requests.get(url = endpoint)
    return response.json()


print(listCategories())