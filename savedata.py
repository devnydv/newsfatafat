import requests 
import json

cat = ["all", "science", "sports", "entertainment", "technology"]
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
    datatodb.reverse()
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
        return "data save krne ki koi jarurat nhi hai"
    else:
        for x in datatodb:
            
            x["id"]= originaldDtaSize
            #print(x["id"])
            saveurl = f'https://filmyapp-e1005.firebaseio.com/news/{category}/data/{originaldDtaSize}.json'
            saved = requests.put(saveurl, json=x)
            originaldDtaSize =originaldDtaSize + 1
            #print(originaldDtaSize)
        
        
            
            