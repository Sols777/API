import requests
import os
from dotenv import load_dotenv
import json
from utils import *
import random


load_dotenv()
# constant
ENDPOINT = os.getenv("ENDPOINT")
# globals

# FUCNTIONS
def getDATA():
    response = requests.get(url=ENDPOINT+'posts')
    data = response.json()
    if response.status_code == 200:
        data = response.json()
        lista = []
        for item in data:
            lista.append({
                'userId' : item['userId'],
                'id': item['id'],
                'title' : item['title'],
                'body' : item['body']
                          })
    return lista
def randomId():
    lista = []
    while len(lista) < 10:
        id = random.randint(1, 100)
        if id not in lista:
            lista.append(id)
    return lista



def printPostId(postsList):
    idList = randomId()
    for post in postsList:
        for id in idList:
            if id == post['id']:
                print(f'''
                        {'*'*100}
                        Post:
                        id: {id}
                        Title: {post['title']}
                        Post: {post['body']}
                        ''')
                response = requests.get(url=ENDPOINT+'posts/'+str(id)+'/'+'comments')
                data = response.json()
                for item in data:
                    print(f'''
                        \nComments:
                        id: {item['postId']}
                        {item['id']} - {item['body']}
                        ''')

# cALLS
postsList = getDATA()
saveJSONFile("JSON/posts.json", postsList)


printPostId(postsList)

