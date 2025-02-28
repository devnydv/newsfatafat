import json
import requests
# from dotenv import load_dotenv
#import os
#load_dotenv()
#db = os.getenv("db")

def filehandle(cate):
    
    db = f'https://filmyapp-e1005.firebaseio.com/news/{cate}/data.json?orderBy="$key"&limitToLast=12'
    
    response = requests.get(db)
    data = response.json()
    rev = list(data.values())
    rev.reverse()
    return rev



def lastd(cate):
    
    db = f'https://filmyapp-e1005.firebaseio.com/news/{cate}/data.json?orderBy="$key"&limitToLast=1'
    response = requests.get(db)
    data = response.json()
    #print(data)
    lastdata= list(data.keys())[0]
    return lastdata

def load (cate, start):
    first = 12
    #db = 'https://filmyapp-e1005.firebaseio.com/news/all/data.json?orderBy="$key"&startAt="1"&endAt="5"'
    db = f'https://filmyapp-e1005.firebaseio.com/news/{cate}/data.json?orderBy="$key"&limitToFirst={first}&startAt="{start}"'
    response = requests.get(db)
    data = response.json()
    
    
    try:
        rev = list(data.values())
        rev.reverse()
        
        return rev
    except:
        return "rev"


def getpost(cate , id):
    db = f'https://filmyapp-e1005.firebaseio.com/news/{cate}/data/{id}.json'
    response = requests.get(db)
    data = response.json()
    return data


    
#page()
