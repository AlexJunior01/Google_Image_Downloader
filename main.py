import bs4
from selenium import webdriver
import sys
import os
import time
from PIL import Image
import requests
import io

def getImagesURL(query:str, max_images:int, driver:webdriver, sleep_time = 1):
    def scrollToEnd(driver, max_images):
        thumbnail_images = driver.find_elements_by_css_selector('img.Q4LuWd')
        number = 0
        while len(thumbnail_images) < max_images:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            thumbnail_images = driver.find_elements_by_css_selector('img.Q4LuWd')

            if number == len(thumbnail_images):
                break
            else:
                number = len(thumbnail_images)

            try:
                load_more_button = driver.find_element_by_css_selector(".mye4qd")
                if load_more_button:
                    driver.execute_script("document.querySelector('.mye4qd').click();")
                    time.sleep(1)
            except:
                continue


    # Resultado da pesquisa
    driver.get('https://www.google.com/imghp')
    search = driver.find_element_by_css_selector('input.gLFyf')
    button = driver.find_element_by_css_selector('button.Tg7LZd')
    search.send_keys('Lua cheia')
    button.click()


    urls = set()
    count = 0

    # Indo até o fim da página
    scrollToEnd(driver, max_images)

    # Miniaturas das imagens
    thumbnail_images = driver.find_elements_by_css_selector('img.Q4LuWd')
    numbers_results = len(thumbnail_images)
    print(f'Found {numbers_results} images. Getting links...')

    for image in thumbnail_images:
        image.click()
        time.sleep(sleep_time)

        #Pegando link
        actual_images = driver.find_elements_by_css_selector('img.n3VNCb')
        for actual_image in actual_images:
            if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                urls.add(actual_image.get_attribute('src'))
                count += 1
        
        if count >= max_images:
            break
    return urls
        
        
def downloadImages(folder, file_names, url):
    for i, url in enumerate(urls):
        path = os.path.join(folder, file_names+f'{i:06d}'+'.jpg')
        try:
            downloadImage(path, url)
        except:
            continue
        
def downloadImage(path, url):
    image = requests.get(url).content
    image_file = io.BytesIO(image)
    save_image = Image.open(image_file).convert('RGB')
    with open(path, 'wb') as file:
        save_image.save(file, 'JPEG', quality=85)
    


if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')


option =  webdriver.FirefoxOptions()
option.add_argument("--no-sandbox")
option.add_argument("--disable-dev-shm-usage")
option.add_argument("--headless")

WEBDRIVER_PATH = '/home/alexjr/Dev/google_img/geckodriver'
driver = webdriver.Firefox(options=option)

query = input('Query: ')
max_images = int(input('Quantas imagens quer baixar?'))
file_names = input('Nome que ira nos arquivos: ')

urls = getImagesURL(query, max_images, driver)
downloadImages('./img', file_names, urls)