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
    mars = mongo.db.mars.find_one()
   #print(mars)
    return render_template("index.html", mars = mars)


@app.route("/scrape")
def scrape():
     #return "Scrape Succesful"
    #mars= {"news_title", "news_p", "featured_image_url", "mars_weather", "html_table", "hemisphere_image_urls"}
    mars = mongo.db.mars
    mars_data = web_scraping.scrape()

    mars.update({}, mars_data, upsert=True)

    return "Scrape Succesful" #redirect("/")

if __name__ == "__main__":
    app.run(debug=True)