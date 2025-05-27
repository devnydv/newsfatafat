"""to make api call"""
import requests
from cachefile import cache
# from dotenv import load_dotenv
#import os
#load_dotenv()
#db = os.getenv("db")
@cache.memoize(600)
def filehandle(cate):
    """get 12 data from from category"""
    db = f'https://filmyapp-e1005.firebaseio.com/news/{cate}/data.json?orderBy="$key"&limitToLast=12'
    response = requests.get(db, timeout=30)
    data = response.json()
    rev = list(data.values())
    rev.reverse()
    return rev



def lastd(cate):
    """ i will update this comment leter"""
    db = f'https://filmyapp-e1005.firebaseio.com/news/{cate}/data.json?orderBy="$key"&limitToLast=1'
    response = requests.get(db, timeout=20)
    data = response.json()
    #print(data)
    lastdata= list(data.keys())[0]
    return lastdata

def load (cate, start):
    """function getting category data from db"""
    first = 12
    #db = 'https://filmyapp-e1005.firebaseio.com/news/all/data.json?orderBy="$key"&startAt="1"&endAt="5"'
    db = f'https://filmyapp-e1005.firebaseio.com/news/{cate}/data.json?orderBy="$key"&limitToFirst={first}&startAt="{start}"'
    response = requests.get(db, timeout=20)
    data = response.json()
    try:
        rev = list(data.values())
        rev.reverse()
        return rev
    except:  
        return "rev"


def getpost(cate , ids):
    """geting a single news"""
    db = f'https://filmyapp-e1005.firebaseio.com/news/{cate}/data/{ids}.json'
    response = requests.get(db, timeout=20)
    data = response.json()
    return data
#page()
