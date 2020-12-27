
import requests
from bs4 import BeautifulSoup 
import re
import urllib3
import time
import random
import csv
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)





                # product_calories = product_soup.find('th', string=re.compile('熱量')).parent.parent.contents[3].contents[3].text




# '''
# 測試區
print('test')
url = 'https://foodtracer.taipei.gov.tw/Front/Breakfast/ProductDetail?id=15042&pt=%e9%a3%b2%e5%93%81%e9%a1%9e'
r = requests.get(url, verify=False)
soup = BeautifulSoup(r.text, 'html.parser')
a = soup.find(string=re.compile('熱量')).parent.next_sibling.next_sibling.text
print(a.strip("kcal大卡 "))
# for i in range(10):
print('test')
# 測試區
# '''