# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:39:57 2021

@author: team
"""

import logging
import requests
from bs4 import BeautifulSoup
# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug')
logger.info('info')
logger.warn('warn')
logger.error('error')
logger.critical('critical')

url = "https://www.nytimes.com/crosswords/game/mini"
response = requests.get(url)

html_icerigi=response.content
dizi=[]
soup=BeautifulSoup(html_icerigi,"html.parser")
for i in soup.find_all("li",{"class":"Clue-li--1JoPu"}):
        dizi.append(i.text)    
across=dizi[0:5]
down=dizi[5:]
print("===ACROSS===")
for x in across:
    print(x)
print("===DOWN===")
for y in down:
    print(y)