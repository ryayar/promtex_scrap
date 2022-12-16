from bs4 import BeautifulSoup
import sqlite3
import requests

'''eMT3105P'''


# search = str(input('Введите запрос: '))

# data = [
#     {'name': 'ebay',
#      'url': f'https://www.ebay.com/sch/i.html?_nkw={search}',
#      'headers': {
#          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#          'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#          # 'cookie': '__uzma=7d7e6aa5-34ad-4971-ab9b-c2a34d5f0b0c; __uzmb=1665122428; __uzme=9887; ak_bmsc=BDE69351A35A7480ADFEEEE87E931765~000000000000000000000000000000~YAAQ5phUaNbEqKqDAQAAzecHsRHHaBz08znQyf1nTtjTszd7wEE+0FLCqsHZkaEHua9vX9wbTt0yjOOryhX8FcxNnXLPmTHO7+cTKz/6DSOLSw4A5YWu+c8uXKpYsCSvWTku/jbmfGspQWk//fpdm6TlrzDgbA6a10KIvz81uW6RWiD2g3hqeo2snJIXYJ7yYSa5hz/d1nzphgiRwpKwNIEI8aWlrpmViIaWz0As+X4BZ7XuUSOcdAl6UUonivJmtidpBicaIip2VlLszX40WkPhVGJKCxsMLVC9IVgSbeNaETwRu0/Et56G7bfhKFaagmVLDwM7iAVFdkCZeCecercyUnkv1Hb6O624lEGHqf2Vis3KvLOL8ddRLphNNIgOSCjaiIiF9Go=; __ssds=2; __ssuzjsr2=a9be0cd8e; __uzmaj2=70d0262c-9ca6-41a7-9326-66087d077d8e; __uzmbj2=1665122429; __uzmcj2=483031316545; __uzmdj2=1665122443; s=CgAD4ACBjQRH8YjEwN2U3MTgxODMwYTBhYzU5NmRiOGRkZmZmZWM5ZTLHgaZw; __deba=hEEc96f1hbYLbmGtL9zT7OXUE4D65wG56t0Nomugy0FBp-l2dJtb4NNuAWd_Vq6SXR8UW1J2_XMwSXzXGqPFGPWECE8w4xAEURq3ia6cIpSe_UqSCs0lJb562l63-cRn-vtfr1u-eDc2rAUTqGhYhg==; __uzmc=376031958458; __uzmd=1665122451; __uzmf=7f6000170ec8ab-1431-4453-adb9-7c9666db3932166512242867623317-5f2cd6951c80696719; ebay=%5Ejs%3D1%5Esbf%3D%23000110%5E; bm_sv=20DA7CF7E29406C2D288D53FE0054310~YAAQ5phUaPbHqKqDAQAA2EkIsRHW8ggpDr3PQGZOoTgFHNxWQ3rACcnzxa0VHrToA2AuKcXchu8pMr5HgkjsFat9tyXxGIXiTfWLkfsr87PU4UFg9pFQf4++H07tfxi+AQob3YGAf6u4a7atL0dZEsFesUt1CZX/AtA0DK5DxtnrWhFUDwAuBZnYimBodDfECViNroWt0UOzg0kW3eENR6FaqNRLrWHBfO8m7I6ENaWejgTe8Rmn2+DpvHQTgg==~1; ns1=BAQAAAYI88/iAAAaAANgASGUg9BY2MDFeMTY2NTEyMjQ1MjAzOV5eMF4yfDR8MTF8N3w1fDNeMV4yXjReM14xMl4xMl4yXjFeMV4wXjBeMF4xXjY0NDI0NTkwNzWSofGAizWUgF1jtT/PORpwGSNyiQ**; dp1=bpbf/%23e000a000000000000000006520f416^bl/RU67022796^; nonsession=BAQAAAYI88/iAAAaAADMABGUg9BYsQ0hOAMoAIGcCJ5ZiMTA3ZTcxODE4MzBhMGFjNTk2ZGI4ZGRmZmZlYzllMgDLAAJjP8eeMTdUmIhVnwmKZwdzlZF6YUQG0d4AcQ**',
#          'cache-control': 'max-age=0',
#          'content-length': '415',
#          'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
#          'sec-ch-ua-full-version': '"103.0.5060.134"',
#          'sec-ch-ua-mobile': '?0',
#          'sec-ch-ua-model': '""',
#          'sec-ch-ua-platform': '"Windows"',
#          'sec-ch-ua-platform-version': '"10.0.0"',
#          'sec-fetch-dest': 'document',
#          'sec-fetch-mode': 'navigate',
#          'sec-fetch-site': 'none',
#          'sec-fetch-user': '?1',
#          'upgrade-insecure-requests': '1',
#          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}},
#     {'name': 'aliexpress',
#      'url': f'https://aliexpress.ru/wholesale?SearchText={search}',
#      'headers': {
#          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#          'accept-language': 'ru-RU,ru;q=0.9',
#          'cache-control': 'max-age=0',
#          'cookie': 'aer_ab=69; aer_abid=7a8ba0432f4d15b3; acs_usuc_t=x_csrf=10z5kn9rd1ftq&acs_rt=fffb94c830574c1798aed82fe7a982a8; xman_t=45ePWKNAKHkESM+oIU6OkHCSSnBFlwvLLCpAxLKY3VOqeuRdeIU0M8fN8pAX3b2Y; xman_f=1CjVnhUws4Mt9F21wv35utUJ4Rni2CRjD8DhtMLygCNsRG/nvwKvVntPgrKkGbXlwLMkdrdj7xZnFL7E7fJZZfgCBrZdux8IRvQEgEmNhmFJ/JYZxk1TGg==; xman_us_f=x_locale=ru_RU&x_l=0&x_c_chg=1&acs_rt=8b646345dde24beab27029683f7cae9c; intl_locale=ru_RU; aep_usuc_f=site=rus&c_tp=RUB&region=RU&b_locale=ru_RU; tmr_lvid=36bc5ee30b8099ada3c97792416b6c59; tmr_lvidTS=1660799726259; tmr_reqNum=2; _ga=GA1.2.717849506.1660799726; _gid=GA1.2.1147906110.1660799726; _gat_UA-164782000-1=1; cna=7riEGwtiIEcCAV9DpyBmJgMG; _ym_uid=1660799726521106285; _ym_d=1660799726; _ym_isad=2; _ym_visorc=b; isg=BD8_wlGdYYtXR2WXC9Ms_3NUzhPJJJPGVS7-sNEM2-414F9i2fQjFr3yIqgeo2s-; l=eBQiSUMnLqsYYj0LBOfanurza77OSIRYYuPzaNbMiOCPO31B5xWlB6YIro86C3MNh6uwR35Wn1oBBeYBqQAonxvTo52LorDmn; tfstk=cYEGB3aQYPu1X8wz3li1m61XzgsRw_-qZorQYO684HKHJe1m-e8yrGWns_1wl; intl_common_forever=c2OlBDj6E42UpE/EiMhZGKVLoLAtl3hN3eMBk7/p3LGIENB/REzbbg==; JSESSIONID=C18764849D2EFA47B5B2DB3448E969C1',
#          'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
#          'sec-ch-ua-mobile': '?0',
#          'sec-ch-ua-platform': '"Windows"',
#          'sec-fetch-dest': 'document',
#          'sec-fetch-mode': 'navigate',
#          'sec-fetch-site': 'none',
#          'sec-fetch-user': '?1',
#          'upgrade-insecure-requests': '1',
#          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}}
# ]


def scrap_ebay(src=''):
    ppp = {}
    position = []
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': '__uzma=7d7e6aa5-34ad-4971-ab9b-c2a34d5f0b0c; __uzmb=1665122428; __uzme=9887; ak_bmsc=BDE69351A35A7480ADFEEEE87E931765~000000000000000000000000000000~YAAQ5phUaNbEqKqDAQAAzecHsRHHaBz08znQyf1nTtjTszd7wEE+0FLCqsHZkaEHua9vX9wbTt0yjOOryhX8FcxNnXLPmTHO7+cTKz/6DSOLSw4A5YWu+c8uXKpYsCSvWTku/jbmfGspQWk//fpdm6TlrzDgbA6a10KIvz81uW6RWiD2g3hqeo2snJIXYJ7yYSa5hz/d1nzphgiRwpKwNIEI8aWlrpmViIaWz0As+X4BZ7XuUSOcdAl6UUonivJmtidpBicaIip2VlLszX40WkPhVGJKCxsMLVC9IVgSbeNaETwRu0/Et56G7bfhKFaagmVLDwM7iAVFdkCZeCecercyUnkv1Hb6O624lEGHqf2Vis3KvLOL8ddRLphNNIgOSCjaiIiF9Go=; __ssds=2; __ssuzjsr2=a9be0cd8e; __uzmaj2=70d0262c-9ca6-41a7-9326-66087d077d8e; __uzmbj2=1665122429; __uzmcj2=483031316545; __uzmdj2=1665122443; s=CgAD4ACBjQRH8YjEwN2U3MTgxODMwYTBhYzU5NmRiOGRkZmZmZWM5ZTLHgaZw; __deba=hEEc96f1hbYLbmGtL9zT7OXUE4D65wG56t0Nomugy0FBp-l2dJtb4NNuAWd_Vq6SXR8UW1J2_XMwSXzXGqPFGPWECE8w4xAEURq3ia6cIpSe_UqSCs0lJb562l63-cRn-vtfr1u-eDc2rAUTqGhYhg==; __uzmc=376031958458; __uzmd=1665122451; __uzmf=7f6000170ec8ab-1431-4453-adb9-7c9666db3932166512242867623317-5f2cd6951c80696719; ebay=%5Ejs%3D1%5Esbf%3D%23000110%5E; bm_sv=20DA7CF7E29406C2D288D53FE0054310~YAAQ5phUaPbHqKqDAQAA2EkIsRHW8ggpDr3PQGZOoTgFHNxWQ3rACcnzxa0VHrToA2AuKcXchu8pMr5HgkjsFat9tyXxGIXiTfWLkfsr87PU4UFg9pFQf4++H07tfxi+AQob3YGAf6u4a7atL0dZEsFesUt1CZX/AtA0DK5DxtnrWhFUDwAuBZnYimBodDfECViNroWt0UOzg0kW3eENR6FaqNRLrWHBfO8m7I6ENaWejgTe8Rmn2+DpvHQTgg==~1; ns1=BAQAAAYI88/iAAAaAANgASGUg9BY2MDFeMTY2NTEyMjQ1MjAzOV5eMF4yfDR8MTF8N3w1fDNeMV4yXjReM14xMl4xMl4yXjFeMV4wXjBeMF4xXjY0NDI0NTkwNzWSofGAizWUgF1jtT/PORpwGSNyiQ**; dp1=bpbf/%23e000a000000000000000006520f416^bl/RU67022796^; nonsession=BAQAAAYI88/iAAAaAADMABGUg9BYsQ0hOAMoAIGcCJ5ZiMTA3ZTcxODE4MzBhMGFjNTk2ZGI4ZGRmZmZlYzllMgDLAAJjP8eeMTdUmIhVnwmKZwdzlZF6YUQG0d4AcQ**',
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
        needed_country = [i.text.replace('от', 'Страна:', 1) for i in needed_body.find_all('span', 's-item__location')]
        needed_quality = [f'Состояние: {i.text}' for i in needed_body.find_all('span', 'SECONDARY_INFO')]
        needed_imgs = [i.get('src') for i in
                       needed_body.find_all('img', 's-item__image-img')]  # можно днлать replace с "l225" на до "l2000"
        needed_price = [i.text.replace('\xa0', ' ') for i in needed_body.find_all('span', 's-item__price')]

        for i in range(0, len(needed_headers)):
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


def delete_all(first_id, last_id):
    for i in range(int(first_id), int(last_id) + 1):
        requests.request('GET', url=f'http://127.0.0.1:8000/dele/{i}')


def scrap_ali(src=''):
    ppp = {}
    position = []

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'aer_ab=69; aer_abid=7a8ba0432f4d15b3; acs_usuc_t=x_csrf=10z5kn9rd1ftq&acs_rt=fffb94c830574c1798aed82fe7a982a8; xman_t=45ePWKNAKHkESM+oIU6OkHCSSnBFlwvLLCpAxLKY3VOqeuRdeIU0M8fN8pAX3b2Y; xman_f=1CjVnhUws4Mt9F21wv35utUJ4Rni2CRjD8DhtMLygCNsRG/nvwKvVntPgrKkGbXlwLMkdrdj7xZnFL7E7fJZZfgCBrZdux8IRvQEgEmNhmFJ/JYZxk1TGg==; xman_us_f=x_locale=ru_RU&x_l=0&x_c_chg=1&acs_rt=8b646345dde24beab27029683f7cae9c; intl_locale=ru_RU; aep_usuc_f=site=rus&c_tp=RUB&region=RU&b_locale=ru_RU; tmr_lvid=36bc5ee30b8099ada3c97792416b6c59; tmr_lvidTS=1660799726259; tmr_reqNum=2; _ga=GA1.2.717849506.1660799726; _gid=GA1.2.1147906110.1660799726; _gat_UA-164782000-1=1; cna=7riEGwtiIEcCAV9DpyBmJgMG; _ym_uid=1660799726521106285; _ym_d=1660799726; _ym_isad=2; _ym_visorc=b; isg=BD8_wlGdYYtXR2WXC9Ms_3NUzhPJJJPGVS7-sNEM2-414F9i2fQjFr3yIqgeo2s-; l=eBQiSUMnLqsYYj0LBOfanurza77OSIRYYuPzaNbMiOCPO31B5xWlB6YIro86C3MNh6uwR35Wn1oBBeYBqQAonxvTo52LorDmn; tfstk=cYEGB3aQYPu1X8wz3li1m61XzgsRw_-qZorQYO684HKHJe1m-e8yrGWns_1wl; intl_common_forever=c2OlBDj6E42UpE/EiMhZGKVLoLAtl3hN3eMBk7/p3LGIENB/REzbbg==; JSESSIONID=C18764849D2EFA47B5B2DB3448E969C1',
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
        needed_body = soup.find('div', 'product-snippet_ProductSnippet__grid__lido9p')
        needed_headers = [i.text for i in needed_body.find_all('div', 'product-snippet_ProductSnippet__name__lido9p')]
        needed_headers_links = [f'https://aliexpress.ru{i.next.get("href").split("?", 1)[0]}' for i in
                                needed_body.find_all('div', 'product-snippet_ProductSnippet__content__lido9p')]

        need_imgs = []
        search_imgs = soup.find_all('div', 'product-snippet_ProductSnippet__container__lido9p')
        for i in search_imgs:
            a = i.find('img', 'gallery_Gallery__image__re6q0q')
            need_imgs.append(f'https:{a.get("src")}')
        needed_imgs = []
        for i in need_imgs:
            try:
                needed_imgs.append(i.replace('https:https:', 'https:'))
            except:
                needed_imgs.append(i)
        # needed_imgs = [f'https:{i.get("src")}' for i in needed_body.find_all('img', 'gallery_Gallery__image__re6q0q')]  # при необхожимости можно играться с размером
        needed_sellers = [i.text for i in
                          needed_body.find_all('div', 'product-snippet_ProductSnippet__caption__lido9p')]
        needed_sellers_links = [f'https:{i.get("href")}' for i in
                                needed_body.find_all('a', 'product-snippet_ProductSnippet__shop__lido9p')]
        needed_price = [i.text for i in needed_body.find_all('div', 'snow-price_SnowPrice__mainM__18x8np')]

        for i in range(0, len(needed_headers)):
            position.append(needed_headers[i])
            position.append(needed_headers_links[i])
            position.append(needed_imgs[i])
            position.append(needed_price[i])

            ppp.setdefault(f'position_{i}', position)
            position = []

        return ppp
#
#
# def print_position(needed_headers=[],
#                    needed_headers_links=[],
#                    needed_imgs=[],
#                    needed_price=[],
#                    needed_sellers=[],
#                    needed_sellers_links=[],
#                    needed_country=[],
#                    needed_quality=[]):
#     for i in range(0, len(needed_headers)):
#
#         try:
#             print(f'Название:               {needed_headers[i]}')
#         except:
#             pass
#         try:
#             print(f'Ссылка на позицию:      {needed_headers_links[i]}')
#         except:
#             pass
#         try:
#             print(f'Ссылка на картинку:     {needed_imgs[i]}')
#         except:
#             pass
#         try:
#             print(f'Цена:                   {needed_price[i]}')
#         except:
#             pass
#         try:
#             print(f'Продавец:               {needed_sellers[i]}')
#         except:
#             pass
#         try:
#             print(f'Ссылка на продавца:     {needed_sellers_links[i]}\n')
#         except:
#             pass
#         try:
#             print(f'Страна:                 {needed_country[i]}')
#         except:
#             pass
#         try:
#             print(f'Состояние:              {needed_quality[i]}\n')
#         except:
#             pass
#
#     print('*' * 70)
#
#
# if search != '':
#     for inc in data:
#         req = requests.get(inc.get('url'), headers=inc.get('headers'))
#         src = req.text
#         if inc.get('name') == 'ebay':
#             scrap_ebay(src)
#         if inc.get('name') == 'aliexpress':
#             scrap_ali(src)
# else:
#     print('Пустой запрос')

# https://193.187.96.247/avito/output.xml
# https://aliexpress.ru/wholesale?SearchText=eMT3105P
