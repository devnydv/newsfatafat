import json
import requests
from dotenv import load_dotenv
#import os
#load_dotenv()
#db = os.getenv("db")



def filehandle(cate):
    db = f'https://filmyapp-e1005.firebaseio.com/news/{cate}.json'
    #print(db)
    response = requests.get(db)
    data = response.json()
    #jdata = json.dumps(data, indent=4)
    alldata = data["data"]
    alldata.reverse()
    return alldata

def getpost(cate , id):
    db = f'https://filmyapp-e1005.firebaseio.com/news/{cate}/data/{id}.json'
    response = requests.get(db)
    data = response.json()
    return data