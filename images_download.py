# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:11:30 2016

@author: User
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
from urllib import request as urllib2
import time
from timeout import timeout

# Enter the name of the files with links. One link per line.
names = ['test.txt']


@timeout(10)
def download(img):
    '''
    Download the image.
    :return:
    '''
    # req = urllib2.Request(img, headers={'User-Agent': header})
    raw_img = urllib2.urlopen(img).read()
    # if 'jpg' in str(raw_img):
    f = open(os.path.join(folder, searchterm, "image_" + str(succounter) + "." + imgtype), "wb")
    f.write(raw_img)
    f.close()


for name in names:
    # Read the links in the text file.
    with open(name) as f:
        searchterms = f.read()
        text = searchterms.splitlines()

    # For each line in the file:
    for searchterm in text:
        print('Searchterm: ', searchterm)
    
        # url = "https://www.google.com.hk/search?q="+searchterm+"&espv=2&biw=1366&bih=613&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi-iavsvbbQAhUGOrwKHTrIAKYQ_AUIBigB"
        url = searchterm
        browser = webdriver.Chrome()
        browser.get(url)
        header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        succounter = 0

        curr_path = os.getcwd()
        folder = curr_path + '/images/'
        if not os.path.exists(folder):
            os.mkdir(folder)    
            
        if not os.path.exists(folder + '/' + searchterm):
            os.mkdir(folder + '/' + searchterm)
        
        for _ in range(500):
            browser.execute_script("window.scrollBy(0,10000)")
            time.sleep(.01)
        
        for x in browser.find_elements_by_xpath("//div[@class='rg_meta']"):    
            print("Count:", succounter)
        
            img = json.loads(x.get_attribute('innerHTML'))["ou"]
            imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
            try:
                print('Img: ', img)
                download(img)
            except Exception:
                print ("Unsuccessful.")
            succounter += 1
        
        print(succounter, "Images successfully downloaded.")
        browser.close()
