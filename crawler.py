import requests
from bs4 import BeautifulSoup 
import re
import urllib3
import time
import random
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# =========================================================
# using requests to "get" a webpage
url = 'https://foodtracer.taipei.gov.tw/Front/Ice/Product?id=54591495'
# r = requests.get("https://opendata.epa.gov.tw/ws/Data/AQI/?$format=json", verify=False)

# print(r.text)

# print(r.status_code)
# print(r.text)

    # print(cat.find('a').get('href')) # 第一個結果是目前頁面 不能用
# print(r.text)


# for producturl in a:
#     url = 'https://foodtracer.taipei.gov.tw' + producturl
#     r = requests.get(url, verify=False)
#     soup = BeautifulSoup(r.text, 'html.parser')

# 連鎖早餐店個別產品熱量
breakfast_indi_url = 'https://foodtracer.taipei.gov.tw/Front/Breakfast/ProductDetail?id=5017&pt=%e4%b8%bb%e9%a4%90'
breakfastr = requests.get(breakfast_indi_url, verify=False)
soup = BeautifulSoup(breakfastr.text, 'html.parser')
attr = {'class': 'store_detail'}
# print(soup.find('th', string='熱量(大卡)').next_sibling.next_sibling)
print(soup.find('th', string='熱量(大卡)').next_sibling.next_sibling.text)
# print(soup.a.next_siblings)
# print(soup.find('div').next_sibling)
# # print(soup.body.contents)
# sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", 'html.parser')
# print(sibling_soup.b.next_sibling)

BeautifulSoup
# 進到摩斯
url = 'https://foodtracer.taipei.gov.tw/Front/Breakfast/Product?id=23928945'
# 先爬目前類別


r = requests.get(url, verify=False)
soup = BeautifulSoup(r.text, 'html.parser')
print(len(soup.find_all('div', class_='panel')))
sub_url = []
for product_tag in soup.find('div', id='mygallery').find_all('div', class_='panel'):
    sub_url.append(product_tag.a['href']) # sub_url: 某個子類別
    print(product_tag.text + '*')
# for url in sub_url: # 開始找產品
#     url = 'https://foodtracer.taipei.gov.tw' + 'url'
#     # r = requests.get(url, verify=False)

#     r = ''
#     while r == '':
#         try:
#             r = requests.get(url, verify=False)
#             break
#         except:
#             print("Connection refused by the server..")
#             print("Let me sleep for 5 seconds")
#             print("ZZzzzz...")
#             time.sleep(5)
#             print("Was a nice sleep, now let me continue...")
#             continue

#     soup = BeautifulSoup(r.text, 'html.parser')
#     product_url = []
#     for product_tag in soup.find_all('div', class_='product'):
#         product_url.append(product_tag.a['href'])
url = 'https://foodtracer.taipei.gov.tw' + sub_url[1]
print(sub_url[1])
# rand = random.randrange(2,5)
# sub_url = [sub_url[0]]
# for url in sub_url:
#     # time.sleep(rand)
#     url = 'https://foodtracer.taipei.gov.tw' + 'url'
#     r = requests.get(url, verify=False)
#     print(r.status_code)

# url = 'https://foodtracer.taipei.gov.tw/Front/Breakfast/ProductDetail?id=5017&pt=%e4%b8%bb%e9%a4%90'
url = 'https://foodtracer.taipei.gov.tw/Front/Breakfast/Product?id=23928945&pt=%e4%b8%bb%e9%a4%90'
r = requests.get(url, verify=False)
print(r.status_code)
# 大分類
    # 商店
        # 商店中分類（panel）
            # 商品



