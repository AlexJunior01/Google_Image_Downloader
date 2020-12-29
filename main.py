import bs4
from selenium import webdriver
import sys
import os
import time

def getImages_URL(query:str, max_images:int, driver:webdriver, sleep_time = 1):
    # Resultado da pesquisa
    driver.get('https://www.google.com/imghp')
    search = driver.find_element_by_css_selector('input.gLFyf')
    button = driver.find_element_by_css_selector('button.Tg7LZd')
    search.send_keys('Lua cheia')
    button.click()

    # Indo até o fim da página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    urls = set()
    count = 0
    results_start = 0  #nao pegar imagens repetidas
    while count < max_images:
        # Miniaturas das imagens
        thumbnail_images = driver.find_elements_by_css_selector('img.Q4LuWd')
        numbers_results = len(thumbnail_images)

        for image in thumbnail_images[results_start:numbers_results]:
            image.click()
            time.sleep(sleep_time)

            #Imagem grande
            actual_images = driver.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    urls.add(actual_image.get_attribute('src'))
                    count += 1
            
        results_start = count
        if count > max_images:
            break
        else:
            show_more_button = driver.find_element_by_css_selector('input.mye4qd')
            if show_more_button:
                show_more_button.click()

    return urls
        
        





if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')


option =  webdriver.FirefoxOptions()
option.add_argument("--no-sandbox")
option.add_argument("--disable-dev-shm-usage")
#option.add_argument("--headless")

WEBDRIVER_PATH = '/home/alexjr/Dev/google_img/geckodriver'
driver = webdriver.Firefox(options=option)

urls = getImages_URL('Lua Cheia', 15, driver, 1)