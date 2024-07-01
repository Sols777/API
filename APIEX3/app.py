import requests
import os
from dotenv import load_dotenv
import json
from utils import *

load_dotenv()

# constants / sensible data

STOCK_NAME = os.getenv("STOCK_NAME")
COMPANY_NAME = os.getenv("COMPANY_NAME")
STOCK_ENDPOINT = os.getenv("STOCK_ENDPOINT")
NEWS_ENDPOINT = os.getenv("NEWS_ENDPOINT")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# globals
stockFileName = "JSON/intraday.json"
newsFileName = "JSON/everything.json"
#
# stockList = loadJSONFile(stockFileName)
# newsList = loadJSONFile(newsFileName)
#
listStocks = []
listIntraDay = []
listNews = []
#
paramsStocks = {
    'function' : 'TIME_SERIES_INTRADAY',
    'symbol' : STOCK_NAME,
    'interval' : '60min',
    'apikey' : STOCK_API_KEY
}
 
#
paramsNews = '''

'''
# functions
        
def getIntraDay():
    params = {
        'function' : 'TIME_SERIES_INTRADAY',
        'symbol' : STOCK_NAME,
        'interval' : '60min',
        'apikey' : STOCK_API_KEY,
        'outputsize' : 'compact'
    }
    response = requests.get(url=STOCK_ENDPOINT, params=params)
    if response.status_code == 200:
        data = response.json()['Time Series (60min)']
        listIntraDay = []
        for item in data.items():
            listIntraDay.append({
                'datetime' : item[0],
                'open' : item[1]['1. open'],
                'high' : item[1]['2. high'],
                'low' : item[1]['3. low'],
                'close' : item[1]['4. close'],
                'volume' : item[1]['5. volume']
            })
    return listIntraDay

def getIntraweek():
    params = {
        'function' : 'TIME_SERIES_WEEKLY',
        'symbol' : STOCK_NAME,
        'apikey' : STOCK_API_KEY,
    }
    listIntraWeek =[]
    response = requests.get(url=STOCK_ENDPOINT, params=params)
    if response.status_code == 200:
        data = response.json()['Weekly Time Series']
        for item in data.items():
            listIntraWeek.append({
                'datetime' : item[0],
                'open' : item[1]['1. open'],
                'close' : item[1]['4. close']
            })
    return listIntraWeek

def findDataByDate(date , intra):
    for item in intra:
        if item['datetime'] == date:
            return item
    
def getStatisticData(date):
    variation = float(date['close'])-float(date['open'])
    variation_perc = (variation / float(date['close']))*100
    return variation, variation_perc

def printWeekStock(intraWeek):
    for day in intraWeek:
        variation, variation_perc = getStatisticData(day)
        print(f"""
            Data: {day['datetime']}
            Abertura: {day['open']}
            Fecho: {day['close']}
            Variação: {variation :.2f}$ ({variation_perc :.2f}%)
            """)

        

def printDayMaxVariation(intraweek):
    max = findDataByDate('2020-08-21',intraweek)
    variation, variation_perc = getStatisticData(max)
    print(f"Day with max variation: {max['datetime']} with  {variation :.2f}$ ({variation_perc :.2f}%)")
    

def getNews():
    params = {
        'apiKey' : NEWS_API_KEY,
        'q' : 'tesla',
        'pageSize' : 3
    }
    response = requests.get(url=NEWS_ENDPOINT, params=params)
    if response.status_code == 200:
        data = response.json()['articles']
        listNews = []
        for item in data:
            print(f'''
                  Title: {item['title']}
                  Author: {item['author']}
                  Description: {item['description']}
                  Url: {item['url']}
                  Data: {item['publishedAt']}
                  ''')
            listNews.append({'Title' : item['title'], 
                         'Author': item['author'],
                         'Description' : item['description'] , 
                         'Url': item['url'],
                         'Data': item['publishedAt']})
        return listNews
    else:
        print('erro')
# call functions

#  ! get intra day stuff
# intraday = getIntraDay()
# saveJSONFile("JSON/intraday.json", intraday)

# dataSaved = "JSON/intraday.json"
#  ! find by date 
# dateToFind = "2024-05-24 19:00:00"
# print(findDataByDate(dateToFind , intraday))
#  ! get week stuff 
# intraWeek = getIntraweek()
# saveJSONFile("JSON/intraWeek.json", intraWeek)
# ! print all stocks formated
# printWeekStock(intraWeek)
# ! prints the max variation stock formated
# printDayMaxVariation(intraWeek)

# !!!! News
# ! 1 get news
news = getNews()
saveJSONFile("JSON/news.json", news)