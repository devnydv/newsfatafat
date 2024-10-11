
from flask import Flask, render_template, request, send_from_directory, redirect 
from api import filehandle, getpost, lastd, load
from newsave import hit
from datetime import datetime

app = Flask(__name__, static_folder='static')


data = filehandle("all")

@app.route("/", methods = ["GET", "POST"])
def fil():
    if request.method == "GET":
        
        reverseddata = data
        cate = request.args.get("category")
        return render_template("card.html", dbdata = reverseddata, cate = cate)
    elif request.method == "POST":
        cate = request.args.get("category")
        postlen = int(lastd(cate)) -11
        page = request.args.get("page", 0 ,type=int)
        start = int(postlen) - 12*page
        print(start)
        loaddata = load(cate, start)
        if loaddata == "rev":
            return "No More news"
        else:
            return render_template("load.html" ,dbdata= loaddata, cat = cate)

    

@app.route("/<cat>/")
def cate(cat):
    data = filehandle(cat)
    #print(start, end)
    return render_template("card.html" , cate = cat, dbdata = data)

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



# Custom Jinja filter to format the date
@app.template_filter('format_date')
def format_date(value):
    try:
        # Convert the string to a datetime object
        date_obj = datetime.strptime(value, '%A, %d %b, %Y')
        # Format it to 'YYYY-MM-DD'
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        return value



if __name__ == "__main__":
    app.run(debug=True)

    # code for index.py
    #from wsgi import app
