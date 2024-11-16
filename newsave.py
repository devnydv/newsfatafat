import requests 
from easygoogletranslate import EasyGoogleTranslate
from datetime import datetime
# CODE TO FETCH only one DATA FROMAPI, TRANSLATE it AND SENT TO DB
def hit():
    def tr(item): 
        translator = EasyGoogleTranslate(
            source_language='en',
            target_language='hi',
            #timeout=10
        )
        result = translator.translate(item)
        return result



    cat = ["all", "science", "sports", "entertainment", "technology"]




    for category in cat:
        dburl = f'https://filmyapp-e1005.firebaseio.com/news/{category}/data.json'
        dbres = requests.get(dburl)
        datafromdb= dbres.json()
    
        originaldDtaSize = len(datafromdb)
        getlsttitle = datafromdb[originaldDtaSize -1]


        if category == "all":
            url = "https://inshorts.com/api/en/news?category=all_news&max_limit=5&include_card_data=true"
            res = requests.get(url)
            maindata = res.json()

       
        #content = tr(maindata["data"]['news_list'][0]["news_obj"]['content'])
       
            orgdate = maindata["data"]['news_list'][0]["news_obj"]['created_at'] /1000
            date_time = datetime.fromtimestamp(orgdate)
            #date = date_time.strftime('%Y-%m-%d %H:%M:%S')
            date = date_time.strftime('%A, %d %B, %Y')
            time = date_time.strftime('%H:%M:%S')
        #imageUrl = maindata["data"]['news_list'][0]["news_obj"]['image_url']
        #readMoreUrl = maindata["data"]['news_list'][0]["news_obj"]['source_url']
        #title = tr(maindata["data"]['news_list'][0]["news_obj"]['title'])
        #url = maindata["data"]['news_list'][0]["news_obj"]['shortened_url']


            news = {"author": maindata["data"]['news_list'][0]["news_obj"]['author_name'],
                "content": tr(maindata["data"]['news_list'][0]["news_obj"]['content']),
                "date" : date,
                "imageUrl" : maindata["data"]['news_list'][0]["news_obj"]['image_url'],
                "readMoreUrl" : maindata["data"]['news_list'][0]["news_obj"]['source_url'],
                "time": time,
                "title" : tr(maindata["data"]['news_list'][0]["news_obj"]['title']),
                "url" : maindata["data"]['news_list'][0]["news_obj"]['shortened_url']
            }
        

        #print(lesssize)
            news["id"] = originaldDtaSize
        
            saveurl = f'https://filmyapp-e1005.firebaseio.com/news/{category}/data/{originaldDtaSize}.json'
            saved = requests.put(saveurl, json = news)
    
        else:
            url = f"https://inshorts.com/api/en/search/trending_topics/{category}?page=1&type=NEWS_CATEGORY"
            res = requests.get(url)
            maindata = res.json()
            

            
            orgdate = maindata["data"]['suggested_news'][0]["news_obj"]['created_at'] /1000
            date_time = datetime.fromtimestamp(orgdate)
            #date = date_time.strftime('%Y-%m-%d %H:%M:%S')
            date = date_time.strftime('%A, %d %B, %Y')
            time = date_time.strftime('%H:%M:%S')
            news = {"author": maindata["data"]['suggested_news'][0]["news_obj"]['author_name'],
                "content": tr(maindata["data"]['suggested_news'][0]["news_obj"]['content']),
                "date" : date,
                "imageUrl" : maindata["data"]['suggested_news'][0]["news_obj"]['image_url'],
                "readMoreUrl" : maindata["data"]["suggested_news"][0]["news_obj"]['source_url'],
                "time": time,
                "title" : tr(maindata["data"]['suggested_news'][0]["news_obj"]['title']),
                "url" : maindata["data"]['suggested_news'][0]["news_obj"]['shortened_url']
            }
        
            # dburl = f'https://filmyapp-e1005.firebaseio.com/news/{category}/data.json'
            # dbres = requests.get(dburl)
            # datafromdb= dbres.json()
    
            # originaldDtaSize = len(datafromdb)
        
        #print(lesssize)

            if getlsttitle["title"] == tr(maindata["data"]['suggested_news'][0]["news_obj"]['title']):
                print("same data found no need to save ")
            else:
                news["id"] = originaldDtaSize
        
                saveurl = f'https://filmyapp-e1005.firebaseio.com/news/{category}/data/{originaldDtaSize}.json'
                saved = requests.put(saveurl, json = news)
