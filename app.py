import json
import math
from flask import Flask, render_template, request, send_from_directory, redirect 
from api import filehandle, getpost
from savedata import hit

app = Flask(__name__, static_folder='static')



data = filehandle("all")
reverseddata = data
postlen = len(reverseddata)


#@app.route("/")
#def index():
    #return render_template("index.html" ,dbdata= data)

@app.route("/")
def fil():
    
    page = request.args.get("page", 0 ,type=int)
    page = page +1
    start = 30*page - 30
    end = 30*page
    #print(start, end)
    tota_page = postlen  / 30
    tota_page = math.ceil(tota_page)
    #print(tota_page)
    cate = request.args.get("category")
    #if cate == None:
        #print(reverseddata[start:1])
    return render_template("index.html",dbdata = reverseddata[start: end], cate = cate, pages= tota_page)
    

@app.route("/<cat>/")
def cate(cat):
    data = filehandle(cat)
    postlen = len(data)
    page = request.args.get("page", 0 ,type=int)
    page = page +1
    start = 30*page - 30
    end = 30*page
    #print(start, end)
    tota_page = postlen  / 30
    tota_page = math.ceil(tota_page)
    data = filehandle(cat)
    return render_template("index.html" , cate = cat, dbdata = data[start: end], pages=tota_page)

@app.route("/news/<cat>/<id>")
def news(cat, id):
    #data = filehandle(cat)
    id = int(id)
    post = getpost(cat, id)

# send 9 items for the recomandation section of read route
    # otherpost = []
    # if id > 9:
    #     newid = id
    #     lowid= newid -9
    #     for x in range(lowid, newid):
    #         #print(x)
    #         otherpost.append([item for item in data if item["id"] == x]) 
    #         #print(otherpost)
    # else:
    #     otherpost = []

    # post contains a single post that is the main post
    #post = [item for item in data if item["id"] == id]
    #print(post)
    return render_template("read.html", ids = id, dbdata = post,  cate = cat)
@app.route("/news/<cat>/<id>/<title>")
def redirt(cat, id, title):
    #data = filehandle(cat)
    id = int(id)
    post = getpost(cat, id)
    return redirect (f"/news/{cat}/{id}")
@app.route("/newdb")
def newdb():
    return render_template("newdb.html", 301)

@app.route("/api")
def saveapi():
    hit()
    return "saved"

@app.route("/source/")
def sour():
    return render_template("credit.html")

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.root_path, 'robots.txt')

if __name__ == "__main__":
    app.run(debug=True)

    # code for index.py
    #from wsgi import app
