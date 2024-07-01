import requests
import beaupy
 
 
def fillListProducts():
    # Devolver 20 produtos ordenados por preço descendente
    endpoint = "https://dummyjson.com/products"
    parameters = {
        'sortBy' : 'price',
        'order' : 'desc',
        'limit' : 0,
        'select' : 'id,title,price,rating,category'
    }
    response = requests.get(url=endpoint, params = parameters)
    return response.json()['products']
 
def printAllComments(listReviews):
    print("\nListagem de Reviews\n")
    for review in listReviews:
        print(f"""
              {review['date'][:10]} - {review['comment']} ({review['rating']}/5)
              by {review['reviewerName']}
              """)
 
def showProductComments(product):
    endpoint = f"https://dummyjson.com/products/{product['id']}"
    response = requests.get(url=endpoint)
    listComments = response.json()["reviews"]
    printAllComments(listComments)
 
def showProducts(listProducts):
    # Selecionar um produto dessa listagem (beaupy) e ver comentários desse produto
    print("\nIndique o produto desejado: \n")
    listProductsBeaupy = [product['title'] for product in listProducts]
    op = beaupy.select(listProductsBeaupy, cursor='->', cursor_style='white', return_index=True)
    showProductComments(listProducts[op])
 
def getAllCategories():
    endpoint = 'https://dummyjson.com/products/categories'
    response = requests.get(url=endpoint)
    return response.json()
 
def getProductsFromCategory(slug, listProducts):
    return [product for product in listProducts if product["category"].lower() == slug]
 
def printAllProductsCategory(listProductsCategory):
    if listProductsCategory:
        for product in listProductsCategory:
            print(f"{product['title']} ({product['rating']}/5)\nPVP: {product['price']}€ Categoria: {product['category']}\n")
    else:
        print("\nNão foram encontrados produtos da categoria definida.\n")
 
 
def getProductsFromCategories(listCategories, listProducts):
    print("\nCategorias\n")
    for category in listCategories[:3]:
        print(f"{category['name']}\n")
        listProductsCategory = getProductsFromCategory(category['slug'], listProducts)
        printAllProductsCategory(listProductsCategory)
        print("*" * 100)
 
 
# globals
listProducts = fillListProducts()
#showProducts(listProducts)
# Ver 10 produtos de cada categoria
listCategories = getAllCategories()
# getProductsFromCategories(listCategories, listProducts)

def getCategoriesStatistics(listCategories, listProducts):
    print("\nCategorias\n")
    for category in listCategories:
        print(f"{category['name']}\n")
        listProductsCategory = getProductsFromCategory(category['slug'], listProducts)
        listProductValues = [product['price'] for product in listProductsCategory]
        listProductRatings = [product['rating'] for product in listProductsCategory]
        #printAllProductsCategory(listProductsCategory)
 
        print(f"Número de produtos: {len(listProductValues)}")
 
        print(f"Valor total: {sum(listProductValues):.2f}€")
 
        print(f"Valor médio: {sum(listProductValues) / len(listProductValues):.2f}€")
 
        mostExpensive = [product for product in listProductsCategory if product['price'] == max(listProductValues)]
        print(f"\nProduto(s) mais caro(s):")
        for product in mostExpensive:
            print(f"{product['title']} ({product['rating']}/5) PVP: {product['price']}€")
 
        lessExpensive = [product for product in listProductsCategory if product['price'] == min(listProductValues)]
        print(f"\nProduto(s) mais barato(s):")
        for product in lessExpensive:
            print(f"{product['title']} ({product['rating']}/5) PVP: {product['price']}€")
 
        bestRating = [product for product in listProductsCategory if product['rating'] == max(listProductRatings)]
        print(f"\nProduto(s) com melhor rating:")
        for product in bestRating:
            print(f"{product['title']} ({product['rating']}/5) PVP: {product['price']}€")
 
        worseRating = [product for product in listProductsCategory if product['rating'] == min(listProductRatings)]
        print(f"\nProduto(s) com pior rating:")
        for product in worseRating:
            print(f"{product['title']} ({product['rating']}/5) PVP: {product['price']}€")
 
        print(f"\nRating médio: {sum(listProductRatings) / len(listProductRatings):.2f}")
        print("*" * 100)
        
getCategoriesStatistics(listCategories,listProducts)