# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:11:30 2016

@author: User
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib2
import time
from timeout import timeout


names = ['gothic_wiki.txt', 'romanesque_wiki.txt', 'renaissance_wiki.txt']

@timeout(10)
def download():
    
    print(img)
    req = urllib2.Request(img, headers={'User-Agent': header})
    raw_img = urllib2.urlopen(req).read()
    f = open(os.path.join(folder, searchterm, "image_" + str(succounter) + "." + imgtype), "wb")
    f.write(raw_img)
    f.close()

    

for name in names:
    with open(name) as f:
        searchterms = f.read()
        text = unicode(searchterms, 'utf-8').splitlines()    
    
    for searchterm in text:
        print(searchterm)
    
        url = "https://www.google.com.hk/search?q="+searchterm+"&espv=2&biw=1366&bih=613&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi-iavsvbbQAhUGOrwKHTrIAKYQ_AUIBigB"
        browser = webdriver.Chrome()
        browser.get(url)
        header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        succounter = 0
        
        folder = r'D:\ConvNet\arch_styles/' + name.replace('_wiki.txt', '')
        if not os.path.exists(folder):
            os.mkdir(folder)    
            
        if not os.path.exists(folder + '/' + searchterm):
            os.mkdir(folder + '/' + searchterm)
        
        for _ in range(500):
            browser.execute_script("window.scrollBy(0,10000)")
            time.sleep(.01)
        
        for x in browser.find_elements_by_xpath("//div[@class='rg_meta']"):    
            print ("Count:", succounter)
#            print ("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])
        
            img = json.loads(x.get_attribute('innerHTML'))["ou"]
            imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
            try:
                download()
            except:
                print ("Unsuccessful.")
            succounter += 1
        
        print (succounter, "Images succesfully downloaded.")
        browser.close()
        
    