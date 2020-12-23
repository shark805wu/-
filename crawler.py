import requests
from bs4 import BeautifulSoup 

# =========================================================
# using requests to "get" a webpage
url = 'https://foodtracer.taipei.gov.tw/Front/Chain'
# r = requests.get("https://opendata.epa.gov.tw/ws/Data/AQI/?$format=json", verify=False)
r = requests.get(url, verify=False) # 不加verify=False的話就爬不了 我也不知道為什麽

print(r.text)

print(r.status_code)

soup = BeautifulSoup(r.text, 'html_parser')
attr = {"class": "store_list"}ㄆ
