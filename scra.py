#!/usr/bin/python

"""
scrap the data and build a nice ready-to-use dataset

ressources :

https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3

"""
import requests # to make http requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
# get the web page where the data is
page = requests.get('https://www.reducmiz.com/resultat_fdj.php?jeu=keno&nb=all')

# create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
# the numbers are in <font> elements
items = soup.find_all('font')
n_rows = len(items)

raw_data = np.zeros((n_rows,71))
i = 0

for item in items:
  indexes = item.text.split()
  for j in range(len(indexes)):
    raw_data[i, int(indexes[j])] = 1
  i+=1

pd.DataFrame(raw_data).to_csv("one-hot.csv")
