import requests 
from easygoogletranslate import EasyGoogleTranslate

# CODE TO FETCH only one DATA FROMAPI, TRANSLATE it AND SENT TO DB

def tr(item): 
    translator = EasyGoogleTranslate(
        source_language='en',
        target_language='hi',
        #timeout=10
    )
    result = translator.translate(item)
    return result
# Output: Dies ist ein Beispiel.



#import json

cat = ["all", "science", "sports", "entertainment", "technology"]
#cat = ["entertainment"]
def hit():
    for category in cat:
        savingdata(category)
        

def savingdata(category):
    
    #get data from api
    
    url = f'https://inshortsapi.vercel.app/news?category={category}'
    res = requests.get(url)
    maindata = res.json()
    main_title= maindata["data"][0]['title']
    datatodb = maindata["data"]
    
    #print(datatodb)

    #get data from database compare and save

    dburl = f'https://filmyapp-e1005.firebaseio.com/news/{category}/data.json'
    dbres = requests.get(dburl)
    datafromdb= dbres.json()
    
    originaldDtaSize = len(datafromdb)
    lesssize = len(datafromdb) -1 
    #print(lesssize)
    data_title = datafromdb[lesssize]['title']
    #print(data_title)
    #if title are save do not add data and if not same save data to db
    if main_title== data_title:
        print("no need to edit...")
    else:
        for x in range(1):
            datatodb[x]["id"] =originaldDtaSize
            transtitle = datatodb[x]["title"]
            transDesc = datatodb[x]['content']
            datatodb[x]["title"] = tr(transtitle)
            datatodb[x]["content"] = tr(transDesc)
            saveurl = f'https://filmyapp-e1005.firebaseio.com/news/{category}/data/{originaldDtaSize}.json'
            saved = requests.put(saveurl, json = datatodb[x])
            originaldDtaSize =originaldDtaSize + 1
            #print(originaldDtaSize)
            print (datatodb[x]["title"])
