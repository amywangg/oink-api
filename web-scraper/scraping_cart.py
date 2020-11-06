#!/usr/bin/env python
# coding: utf-8

# In[1]:


import codecs
import json
import re
import requests
from bs4 import BeautifulSoup


def scrape_cart(file):
    try:
        # from here on we are going to use our own html code because we can't seem to open and add something to shopping cart through our script
        our_page = codecs.open(file, 'r') 
        soup = BeautifulSoup(our_page, 'html.parser')


        # all products in cart are within this div tag
        products = soup.findAll("div",{"class":"sc-list-item-content"})

        # initialize dictionary for all product info
        appendix={}

        # loop through all products in the cart and get their link, item code, name, price
        for each in products:
            link = "https://www.amazon.ca" + each.div.find("a",{"class":"a-link-normal sc-product-link"})['href']

            sub_code= re.sub(r'^.*?product/', '', link)
            code = sub_code[:sub_code.find("/ref")]

            # categories will be added in next sprint when we deal with Amazon API
            # item_link_response = requests.get('https://api.rainforestapi.com/request?api_key=B4057000DCF0420D8944FE2D7CFCF6B9&type=product&amazon_domain=amazon.ca&asin=' + code)
            # category = []
            # for each in item_link_response.json()['product']['categories']:
                # category.append(each['name'])
            
            name = re.sub('\s+',' ',each.div.find("span",{"class":"a-size-medium sc-product-title a-text-bold"}).text)
            price = re.sub('\s+',' ',each.div.find("span",{"class":"a-size-medium a-color-base sc-price sc-white-space-nowrap sc-product-price a-text-bold"}).text)


            appendix.update({
                code:{
                    "link" : link,
                    "name" : name,
                    "price" : price,
                    # "category" : category
                }
            })
        
        
        return True
    except:
        return False


# # Resources
# 
# https://www.youtube.com/watch?v=mKxFfjNyj3c&ab_channel=edureka%21
# https://www.dataquest.io/blog/web-scraping-beautifulsoup/
