import requests
import os
from dotenv import load_dotenv
from random import randint
 
load_dotenv()
ENDPOINT = os.getenv("ENDPOINT")
 
def generateRandomList(total):
    temp = []
    for _ in range(total):
        val = randint(1,100)
        if val not in temp:
            temp.append(val)
    return temp
 
def printPost(index):
    # https://jsonplaceholder.typicode.com/posts/1
    response = requests.get(f"{ENDPOINT}/posts/{index}")
    if response.status_code == 200:
        # post
        post = response.json()
        print(f"Título: {post['title']}")
        print(f"Descrição: {post['body'].strip()}\n\n")
    else:
        print("\nErro!\n")
   
    # comments do post
    print("\nComentários:\n")
    # https://jsonplaceholder.typicode.com/posts/1/comments
    response = requests.get(f"{ENDPOINT}/posts/{index}/comments")
    if response.status_code == 200:
        listComments = response.json()
        for comment in listComments:
            print(f"Nome: {comment['name']}")
            print(f"Comentário: {comment['body']}\n")
    else:
        print("\nErro!\n")
 
def getPosts():
    randomIDList = generateRandomList(1)
    print("Listagem de Posts aleatórios e respetivos comentários\n")
    for index in randomIDList:
        printPost(index)
 
def getTodos(userID):
    # buscar todos os todos
    # https://jsonplaceholder.typicode.com/todos
    response = requests.get(f"{ENDPOINT}/todos")
    print(response)
    if response.status_code in (200, 201, 204):
        allTodos = response.json()
        # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
        # get all TODOS from userID
        todosUser = [todo for todo in allTodos if todo['userId'] == userID]
        completedTodos = [todo for todo in todosUser if todo['completed']]
        incompletedTodos = [todo for todo in todosUser if not todo['completed']]
        print(f"Total de TODOS do user: {len(todosUser)}")
        print(f"Total de TODOS realizados do user: {len(completedTodos)}")
        print(f"Total de TODOS não realizados do user: {len(incompletedTodos)}")
        print("\nListagem de TODOS: \n")
        for todo in todosUser:
            print(f"{todo['title']}")
            todo['completed'] = "Sim" if todo['completed'] else "Não"
            print(f"Todo realizado: {todo['completed']}")
    else:
        print("\nErro: no todos!\n")
 
def getThumbnailUrl(albumId):
    # https://jsonplaceholder.typicode.com/photos
    response = requests.get(f"{ENDPOINT}/photos")
    allPhotos = response.json()
    albumPhotos = [photo['thumbnailUrl'] for photo in allPhotos if photo['albumId'] == albumId]
    return albumPhotos
 
def getThumbnailUrlParams(albumId):
    params = {
        "albumId" : albumId
    }
    response = requests.get(f"{ENDPOINT}/photos", params=params)
    albumPhotos = response.json()['thumbnailUrl']
   
    return albumPhotos    
 
#getPosts()
#getTodos(3)
thumbnailUrlList = getThumbnailUrl(16)
#thumbnailUrlList = getThumbnailUrlParams(16)
print(thumbnailUrlList)