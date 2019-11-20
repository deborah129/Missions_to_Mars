#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pymongo
import pandas as pd
import time


# In[38]:


#get_ipython().system('which chromedriver')


# In[39]:
def init_browser():

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)



# In[40]:
def scrape():
    browser = init_browser()
    mars_data = {}
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)



#Retrieve latest news

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p
     
    #print(news_title, news_p)



    url ='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)



    browser.find_by_id("full_image").click()
    time.sleep(2)
    browser.click_link_by_partial_text("more info")
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    featured_image_url_1 = soup.find('img', class_='main_image')['src']
    #print(featured_image_url_1)



    featured_image_url_2 = 'https://www.jpl.nasa.gov'
    featured_image = featured_image_url_2 + featured_image_url_1
#     #print(featured_image_url)
    mars_data['featured_image'] = featured_image

#Mars Weather: Scraping from latest weather tweet
   
    url ='https://twitter.com/marswxreport?lang=en'
    browser.visit(url)



    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')



    mars_weather = soup.find('div', class_='js-tweet-text-container').p.text
  # print(mars_weather)
    mars_data["mars_weather"] = mars_weather

#Table about Mars facts

    url = 'https://space-facts.com/mars/'
    browser.visit(url)


    tables = pd.read_html(url)
   
    df = tables[0]
    #df


    df.columns =['Description', 'Values']
    #df

    html_table = df.to_html()
    #html_table
    mars_data["html_table"] = html_table



    hemisphere_image_urls = [{"title": " Valley Marineris Hemisphere""https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"}]
    mars_data["hemispheres"]= hemisphere_image_urls
   




# # #main_url = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking"
# # #hemispheres_urls = ["valles_marineris_enhanced.tif/full.jpg", "cerberus_enhanced.tif/full.jpg","schiaparelli_enhanced.tif/full.jpg", "syrtis_major_enhanced.tif/full.jpg"]

# # #for h in hemispheres_urls:
# #    # img_url = main_url + h

# # #titles = ["Valley Marineris Hemisphere", "Cerberus Hemisphere", "Schiaparelli Hemisphere", "Syrtis Major Hemisphere"]
    

    

    browser.quit()
    return mars_data