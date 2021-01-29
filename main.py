# Bibliotecas utilizadas no scrap
import bs4
from selenium import webdriver
import sys
import os
import time

# Bibliotecas utilizadas no download
from PIL import Image
import requests
import io


def iniciarWebDriver(query:str, max_images:int):
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
    
    
    # Configurações do webdriver
    option =  webdriver.FirefoxOptions()
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--headless")

    # Indo até o Google Imagens
    driver = webdriver.Firefox(options=option)
    driver.get('https://www.google.com/imghp')

    # Pesquisando
    search = driver.find_element_by_css_selector('input.gLFyf')
    button = driver.find_element_by_css_selector('button.Tg7LZd')
    search.send_keys(query)
    button.click()

    # Indo até o fim da página
    scrollToEnd(driver, max_images)
    return driver


def getImagesURL(max_images:int, driver:webdriver, sleep_time = 1):
    urls = list()
    count = 0

    # Miniaturas das imagens
    thumbnail_images = driver.find_elements_by_css_selector('img.Q4LuWd')
    numbers_results = len(thumbnail_images)
    print(f'{numbers_results} imagens encontradas. Pegando os links...')

    for image in thumbnail_images:
        image.click()
        time.sleep(sleep_time)

        # Pegando link
        actual_images = driver.find_elements_by_css_selector('img.n3VNCb')
        for actual_image in actual_images:
            if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                if actual_image.get_attribute('src') not in urls:
                    urls.append(actual_image.get_attribute('src'))
                    count += 1
        
        if count >= max_images:
            break
    return urls
        
        
def downloadImages(folder, file_names, urls):
    qtd_imagens = 0

    if not os.path.exists(folder):
        os.makedirs(folder)

    for i, url in enumerate(urls):
        path = os.path.join(folder, file_names+f'{i:06d}'+'.jpg')
        try:
            downloadImage(path, url)
            qtd_imagens += 1
        except:
            continue
    
    print(f'{qtd_imagens} imagens foram baixadas!')


def downloadImage(path, url):
    image = requests.get(url).content
    image_file = io.BytesIO(image)
    save_image = Image.open(image_file).convert('RGB')
    with open(path, 'wb') as file:
        save_image.save(file, 'JPEG', quality=85)
    

def main():
    if os.environ.get('DISPLAY','') == '':
        os.environ.__setitem__('DISPLAY', ':0.0')

    query = input('Query: ')
    max_images = int(input('Múmero de imagens: '))
    file_names = input('Nome que ira nos arquivos: ')
    folder = input('Nome da pasta: ')

    driver = iniciarWebDriver(query, max_images)
    urls = getImagesURL(max_images, driver)
    downloadImages(folder, file_names, urls)


main()