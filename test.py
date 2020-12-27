
import requests
from bs4 import BeautifulSoup 
import re
import urllib3
import time
import random
import csv
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)









# '''
# 測試區
print('test')
url = 'https://foodtracer.taipei.gov.tw/Front/Ice/ProductDetail?id=6568&pt=%e5%a5%b6%e9%a6%99%e7%b3%bb%e5%88%97'
r = requests.get(url, verify=False)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.find(string=re.compile('熱量')).parent.parent.contents[4].text.strip())
# for i in range(10):
print('test')
# 測試區
# '''