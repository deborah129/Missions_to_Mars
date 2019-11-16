from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import web_scraping
import sys
print(sys.path)

#create an instance  of flask
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)



@app.route("/")
def home():
    data = mongo.db.data.find()
   #print(mars)
    return render_template("index.html", data = "data")


@app.route("/scrape")
def scrape():
    #mars= {"news_title", "news_p", "featured_image_url", "mars_weather", "html_table", "hemisphere_image_urls"}
    #return render_template("index.html", text = "")
    data = web_scraping.scrape_info()

    mongo.db.data.update({}, data, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)