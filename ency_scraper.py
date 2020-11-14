##Dependencies##
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import selenium
import time
import csv

##Scrape##
#Start driver and navigate to webpage
wd = webdriver.Chrome(chrome_options=options)
url = "https://www.thezorklibrary.com/history/00-encyclopedia.html"
wd.get(url) 
#Create empty collections
itemlist=[]
contentlist=[]
frobozzica={}

#Generate List of Links
for i in range(30, 2373):
    try:
        links=wd.find_elements_by_tag_name('a')
    #------->Assign link as item name to a variable
        item=links[i].text
        itemlist.append(item)
    #------->click the link
        links[i].click()
    #------->grab the body text
        body = wd.find_element_by_tag_name('body')
        unstriped=body.text
        content= (unstriped.rstrip("\n"))
    #------->save body text to content list
        contentlist.append(content)
    #------->create a dictionary entry with [entry name: link text]
        frobozzica[item] = content
    #------->go back to the main page and wait
        wd.get(url)
    except:
        continue
