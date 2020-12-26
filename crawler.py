import requests
from bs4 import BeautifulSoup 
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# =========================================================
# using requests to "get" a webpage
url = 'https://foodtracer.taipei.gov.tw/Front/Ice/Product?id=54591495'
# r = requests.get("https://opendata.epa.gov.tw/ws/Data/AQI/?$format=json", verify=False)
r = requests.get(url, verify=False) # 不加verify=False的話就爬不了 我也不知道為什麽

# print(r.text)

# print(r.status_code)
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
# attr = {"class": "store_list"}
# # print(soup.prettify)
# for link in soup.find_all('a'):
#     print(link.get('href'))
# print(soup.find_all('a'))
categories = soup.find_all(class_="panel")
# print(categories)
a = [] # 各產品網址

for cat in categories:
    a.append(cat.find('a').get('href'))
    # print(cat.find('a').get('href')) # 第一個結果是目前頁面 不能用
# print(r.text)


# for producturl in a:
#     url = 'https://foodtracer.taipei.gov.tw' + producturl
#     r = requests.get(url, verify=False)
#     soup = Beautifulsoup(r.text, 'html.parser')

# 連鎖早餐店個別產品熱量
breakfast_indi_url = 'https://foodtracer.taipei.gov.tw/Front/Breakfast/ProductDetail?id=5017&pt=%e4%b8%bb%e9%a4%90'
breakfastr = requests.get(breakfast_indi_url, verify=False)
soup = BeautifulSoup(breakfastr.text, 'html.parser')
attr = {'class': 'store_detail'}
print(soup.find('th', string='熱量(大卡)').next_sibling.next_sibling)
# print(soup.a.next_siblings)
# print(soup.find('div').next_sibling)
# # print(soup.body.contents)
# sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", 'html.parser')
# print(sibling_soup.b.next_sibling)