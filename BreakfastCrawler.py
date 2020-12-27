import requests
from bs4 import BeautifulSoup 
import re
import urllib3
import time
import random
import csv
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

strip = "kcal大卡 "

calories_dic = {}
with open('finalcsv.csv', newline='') as csvfile:
    csv = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in csv:
        count += 1
        if count < 92:
            continue
        print(count)
        time.sleep(3)
        if count == 110:
            break
        store_name = row[0]
        store_url = row[1]
        calories_dic[store_name] = {}
        product_url_list = []
        store_r = requests.get(store_url, verify=False)
        store_soup = BeautifulSoup(store_r.text, 'html.parser')
        sub_url_list = []
        for product_tag in store_soup.find('div', id='mygallery').find_all('div', class_='panel'):
            sub_url_list.append(product_tag.a['href']) # sub_url_list: 某個子類別
        for sub_url in sub_url_list: # 開始找產品
            sub_url = 'https://foodtracer.taipei.gov.tw' + sub_url
            sub_r = requests.get(sub_url, verify=False)
            sub_soup = BeautifulSoup(sub_r.text, 'html.parser')
            for product_tag in sub_soup.find_all('div', class_='product'):
                product_url_list.append(product_tag.a['href'])

        # 以下大類別不同（速食/冰...）要改
        for product_url in product_url_list:
            try:
                product_url = 'https://foodtracer.taipei.gov.tw' + product_url
                product_r = requests.get(product_url, verify=False)
                product_soup = BeautifulSoup(product_r.text, 'html.parser')
                product_name = product_soup.find('div', class_='crack').a.next_sibling.strip('\n \r /') # 品名


                product_calories = product_soup.find('th',  string=re.compile('熱量')).next_sibling.next_sibling.text
                calories_dic[store_name][product_name] = float(product_calories.strip(strip))
            except:
                try:
                    product_calories = product_soup.find('span',  string=re.compile('熱量')).next_sibling.next_sibling.text
                    calories_dic[store_name][product_name] = float(product_calories.strip(strip))
                except:
                    print(product_url, product_name)


print(calories_dic)