from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests


def scrap_ebay(src='', dollar_rate=57.5, our_course=100):
    ppp = {}
    position = []
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-length': '415',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-full-version': '"103.0.5060.134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    if not src == '':
        req = requests.get(f'https://www.ebay.com/sch/i.html?_nkw={src}', headers=headers)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')
        needed_body = soup.find('div', 'srp-river-results')
        needed_headers = [i.text for i in needed_body.find_all('span', attrs={'role': 'heading'})]
        needed_headers_links = [i.get('href').split('?', 1)[0] for i in needed_body.find_all('a', 's-item__link')]
        needed_country = [i.text.replace('от', '', 1) for i in needed_body.find_all('span', 's-item__location')]
        needed_quality = [f'{i.text}' for i in needed_body.find_all('span', 'SECONDARY_INFO')]
        needed_imgs = [i.get('src') for i in
                       needed_body.find_all('img', 's-item__image-img')]  # можно днлать replace с "l225" на до "l2000"
        prices = [i.text.replace('\xa0', '').replace('руб.', '').split(',')[0] for i in
                        needed_body.find_all('span', 's-item__price')]
        # формула пересчета цены
        needed_price = []
        for price in prices:
            try:
                price = int(price)
                if price < 100:
                    price = 100

                priceUSD = price / dollar_rate
                if priceUSD < 250:
                    price = priceUSD * our_course * 2
                elif priceUSD < 500:
                    price = 500 * our_course
                else:
                    price = priceUSD * our_course
                needed_price.append(f'{int(price)},00 р/шт')
            except:
                needed_price.append(f'{price},00 р/шт')

        for i in range(0, len(needed_headers)):
            position.append('Ebay')
            position.append(needed_headers[i])
            position.append(needed_headers_links[i])
            position.append(needed_imgs[i])
            position.append(needed_price[i])
            position.append(needed_country[i])
            try:
                position.append(needed_quality[i])
            except:
                pass
            ppp.setdefault(f'position_{i}', position)
            position = []

        return ppp


def scrap_ali(src='', dollar_rate=57.5, our_course=100):
    ppp = {}
    position = []
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    if not src == '':
        req = requests.get(f'https://aliexpress.ru/wholesale?SearchText={src}', headers=headers)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')
        needed_body = soup.find('div', re.findall(r'product-snippet_ProductSnippet__grid__\S{6}', src))
        needed_headers = [i.text for i in needed_body.find_all('div', re.findall(
            r'product-snippet_ProductSnippet__name__\S{6}', src))]
        needed_headers_links = [f'https://aliexpress.ru{i.next.get("href").split("?", 1)[0]}' for i in
                                needed_body.find_all('div',
                                                     re.findall(r'product-snippet_ProductSnippet__content__\S{6}',
                                                                src))]

        need_imgs = []
        search_imgs = soup.find_all('div', re.findall(r'product-snippet_ProductSnippet__container__\S{6}', src))
        for i in search_imgs:
            a = i.find('img', re.findall(r'gallery_Gallery__image__\S{6}', src))
            need_imgs.append(f'https:{a.get("src")}')
        needed_imgs = []
        for i in need_imgs:
            try:
                needed_imgs.append(i.replace('https:https:', 'https:'))
            except:
                needed_imgs.append(i)
        needed_sellers = [i.text for i in
                          needed_body.find_all('div',
                                               re.findall(r'product-snippet_ProductSnippet__caption__\S{6}', src))]
        needed_sellers_links = [f'https:{i.get("href")}' for i in
                                needed_body.find_all('a',
                                                     re.findall(r'product-snippet_ProductSnippet__shop__\S{6}', src))]
        prices = [i.text.replace(' ', '').replace('руб.', '').split(',')[0] for i in needed_body.find_all('div',
                                                             re.findall(r'snow-price_SnowPrice__mainM__\S{6}', src))]
        # формула пересчета цены
        needed_price = []
        for price in prices:
            price = int(price)
            if price < 100:
                price = 100

            priceUSD = price / dollar_rate
            if priceUSD < 250:
                price = priceUSD * our_course * 2
            elif priceUSD < 500:
                price = 500 * our_course
            else:
                price = priceUSD * our_course
            needed_price.append(f'{int(price)},00 р/шт')

        for i in range(0, len(needed_headers)):
            position.append('AliExpress')
            position.append(needed_headers[i])
            position.append(needed_headers_links[i])
            position.append(needed_imgs[i])
            position.append(needed_price[i])
            position.append('Китай')

            ppp.setdefault(f'position_{i}', position)
            position = []

        return ppp


def scrap_avito(src='', dollar_rate=57.5, our_course=100):
    ppp = {}
    position = []
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless") # безголовый хром
    driver = webdriver.Chrome(executable_path='chromeDriver/chromedriver.exe', options=options)
    driver.get(f"https://www.avito.ru/all?q={src}")
    html = driver.find_element(By.TAG_NAME, 'html')
    for i in range(0, 15):
        html.send_keys(Keys.PAGE_DOWN) # нужно, так как картинки за экраном не прогружаются
    src = driver.page_source
    driver.close()

    soup = BeautifulSoup(src, 'lxml')
    name = [i.text.strip() for i in soup.find_all(attrs={'itemprop': 'name'})]
    link = [f"https://www.avito.ru{i.get('href')}" for i in soup.find_all(attrs={'data-marker': 'item-title'})]
    image = [i.next.get('src') for i in soup.find_all('div', re.findall(r'photo-slider-item-\S{4,6}', src))]
    prices = [i.get('content') for i in soup.find_all(attrs={'itemprop': 'price'})]
    city = [i.next.next.text for i in soup.find_all('div', re.findall(r'geo-root-\S{4,6}', src))]

    # формула пересчета цены
    needed_price = []
    for price in prices:
        price = int(price)
        if price < 100:
            price = 100

        priceUSD = price / dollar_rate
        if priceUSD < 250:
            price = priceUSD * our_course * 2
        elif priceUSD < 500:
            price = 500 * our_course
        else:
            price = priceUSD * our_course
        needed_price.append(f'{int(price)},00 р/шт')

    for i in range(0, len(name)):
        position.append('Avito')
        position.append(name[i])
        position.append(link[i])
        position.append(image[i])
        position.append(needed_price[i])
        position.append(city[i])

        ppp.setdefault(f'position_{i}', position)
        position = []

    return ppp


def delete_all(first_id, last_id):
    for i in range(int(first_id), int(last_id) + 1):
        requests.request('GET', url=f'http://127.0.0.1:8000/dele/{i}')
