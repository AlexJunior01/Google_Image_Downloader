import bs4
from selenium import webdriver
import sys
import os
import time
import urllib.request

def downloadImages(folder, file_names, urls):
    for i, url in enumerate(urls):
        path = os.path.join(folder, file_names, f'{i:06d}'+'.jpg')
        urllib.request.urlretrieve(url, filename=path)




path = os.path.join('./img', 'lua_cheia'+f'{5:02d}')
url = 'https://p2.trrsf.com/image/fget/cf/940/0/images.terra.com/2020/09/30/saiba-quais-as-previsoes-pra-lua-cheia-que-se-aproxima-15993.jpg'
urllib.request.urlretrieve(url, filename=path)