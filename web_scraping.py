#!/usr/bin/env python
# coding: utf-8



#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

import ssl

ssl._create_default_https_context = ssl._create_unverified_context





#get_ipython().system('which chromedriver')

def init_browser():

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


# In[40]:
def scrape_info():

    browser = init_browser()
    data = {}
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    
    print(url)
    browser.visit(url)





    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    
    data['news_title']= news_title
    data['news_p'] = news_p
     
    #print(news_title, news_p)

    # browser.quit()

    # browser = init_browser()
    url ='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    print(url)
    browser.visit(url)



    browser.find_by_id("full_image").click()
    time.sleep(2)
    browser.click_link_by_partial_text("more info")
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    featured_image_url_1 = soup.find('img', class_='main_image')['src']
    #print(featured_image_url_1)



    featured_image_url_2 = 'https://www.jpl.nasa.gov'
    featured_image_url = featured_image_url_2 + featured_image_url_1
    #print(featured_image_url)
    data['featured_image_url'] = featured_image_url
    # browser.quit()

    # browser = init_browser()
    url ='https://twitter.com/marswxreport?lang=en'
    print(url)
    browser.visit(url)



    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')



    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
   #print(mars_weather)
    data['mars_weather']= mars_weather

   
    url = 'https://space-facts.com/mars/'





    tables = pd.read_html(url)
   #tables




    #type(tables)



    df = tables[0]
    #df





    df.columns =['Description', 'Values']
    #df




    html_table = df.to_html()
    #html_table
    data['html_table'] = html_table



    data["hemisphere_image_urls"] = [{"title": " Valley Marineris Hemisphere""https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"}]

    #data = {"news_title": news_title, "news_p": news_p, "featured_image_url": featured_image_url, "weather": html_table, "images": hemisphere_image_urls }




#main_url = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking"
#hemispheres_urls = ["valles_marineris_enhanced.tif/full.jpg", "cerberus_enhanced.tif/full.jpg","schiaparelli_enhanced.tif/full.jpg", "syrtis_major_enhanced.tif/full.jpg"]

#for h in hemispheres_urls:
   # img_url = main_url + h

#titles = ["Valley Marineris Hemisphere", "Cerberus Hemisphere", "Schiaparelli Hemisphere", "Syrtis Major Hemisphere"]
    

    

    # browser.quit()
    return data