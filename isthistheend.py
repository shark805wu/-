import requests
from bs4 import BeautifulSoup 
import re
import urllib3
import time
import csv
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

calories_dic = {}
skip = [13,91,110]
skip_list = ['https://foodtracer.taipei.gov.tw/Front/Breakfast/ProductDetail?id=1677&pt=%e5%a4%aa%e5%8f%a4%e9%a3%b2%e5%93%81', 'https://foodtracer.taipei.gov.tw/Front/Breakfast/ProductDetail?id=1725&pt=%e5%a4%aa%e5%8f%a4%e9%a3%b2%e5%93%81', 'https://foodtracer.taipei.gov.tw/Front/Breakfast/ProductDetail?id=10069&pt=%e5%a4%aa%e5%8f%a4%e9%a3%b2%e5%93%81', 'https://foodtracer.taipei.gov.tw/Front/Breakfast/ProductDetail?id=10070&pt=%e5%a4%aa%e5%8f%a4%e9%a3%b2%e5%93%81', 'https://foodtracer.taipei.gov.tw/Front/Breakfast/ProductDetail?id=19866&pt=%e5%a4%aa%e5%8f%a4%e9%a3%b2%e5%93%81', 'https://foodtracer.taipei.gov.tw/Front/Breakfast/ProductDetail?id=10109&pt=%e9%9b%80%e5%b7%a2%e9%a3%b2%e5%93%81']
strip = 'kcal大卡約 '
with open('finalcsv.csv', newline='', encoding='utf-8') as csvfile:
    csv = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in csv:
        count += 1
        if count in skip:
            continue
        # store_name = roe[0]
        store_url = row[1]
        product_url_list = []
        store_r = requests.get(store_url, verify=False)
        store_soup = BeautifulSoup(store_r.text, 'html.parser')
        sub_url_list = []
        for product_tag in store_soup.find('div', id='mygallery').find_all('div', class_='panel'):
            sub_url_list.append(product_tag.a['href'])
        for sub_url in sub_url_list:
            sub_url = 'https://foodtracer.taipei.gov.tw' + sub_url
            sub_r = requests.get(sub_url, verify=False)
            sub_soup = BeautifulSoup(sub_r.text, 'html.parser')
            for product_tag in sub_soup.find_all('div', class_='product'):
                product_url_list.append(product_tag.a['href'])

        for product_url in product_url_list:
            product_url = 'https://foodtracer.taipei.gov.tw' + product_url
            if product_url in skip_list:
                continue
            product_r = requests.get(product_url, verify=False)
            product_soup = BeautifulSoup(product_r.text, 'html.parser')
            try:
                store_name = product_soup.find('div', class_='storeName').text
            except:
                print(product_url)
            if store_name not in calories_dic:
                calories_dic[store_name] = {}
            product_name = product_soup.find('div', class_='crack').a.next_sibling.strip('\n \r/') # 品名

            if count < 13: # 速食
                try:
                    product_calories = product_soup.find('th', string=re.compile('熱量')).parent.parent.contents[3].contents[3].text
                    calories_dic[store_name][product_name] = float(product_calories)
                except:
                    pass

            if 13 < count < 91: # 飲冰品
                try:
                    parenttag = product_soup.find(string=re.compile('熱量')).parent.parent
                    try:
                        if len(parenttag) == 7:
                            product_calories = product_soup.find(string=re.compile('熱量')).parent.parent.contents[4].text.strip()
                            calories_dic[store_name][product_name] = float(product_calories.strip('蔗度熱量正常冰全糖熱量(大卡) kcal'))

                        if len(parenttag) == 13:
                            product_name_one = product_name + product_soup.find(string=re.compile('熱量')).parent.parent.contents[2].text
                            product_calories_one = product_soup.find(string=re.compile('熱量')).parent.parent.contents[4].text
                            calories_dic[store_name][product_name_one] = float(product_calories_one.strip('蔗度熱量正常冰全糖熱量約(大卡) kcal'))
                            product_name_two = product_name + product_soup.find(string=re.compile('熱量')).parent.parent.contents[8].text
                            product_calories_two = product_soup.find(string=re.compile('熱量')).parent.parent.contents[10].text
                            calories_dic[store_name][product_name_two] = float(product_calories_two.strip('蔗度熱量正常冰全糖熱量(大卡) kcal'))
                    except:
                        if len(parenttag) == 7 and "/" in product_calories:
                            calories_list = product_calories.split("/")
                            capacity_list = product_soup.find(string=re.compile('熱量')).parent.parent.contents[2].text.split("/")
                            product_name_one = product_name + capacity_list[0]
                            product_name_two = product_name + capacity_list[1]
                            calories_dic[store_name][product_name_one] = float(calories_list[0].strip('蔗度熱量正常冰全糖熱量約(大卡) kcal中'))
                            calories_dic[store_name][product_name_two] = float(calories_list[1].strip('蔗度熱量正常冰全糖熱量約(大卡) kcal中'))
                        if len(parenttag) == 7 and ", " in product_calories:
                            calories_list = product_calories.split(", ")
                            capacity_list = product_soup.find(string=re.compile('熱量')).parent.parent.contents[2].text.split(", ")
                            product_name_one = product_name + capacity_list[0]
                            product_name_two = product_name + capacity_list[1]
                            calories_dic[store_name][product_name_one] = float(calories_list[0].strip('蔗度熱量正常冰全糖熱量約(大卡) kcal中'))
                            calories_dic[store_name][product_name_two] = float(calories_list[1].strip('蔗度熱量正常冰全糖熱量約(大卡) kcal中'))
                except:
                    pass
                    # print(product_calories)

            if 91 < count < 110:
                try:
                    product_calories = product_soup.find('th',  string=re.compile('熱量')).next_sibling.next_sibling.text
                    calories_dic[store_name][product_name] = float(product_calories.strip("kcal大卡 "))
                except:
                    try:
                        product_calories = product_soup.find(string=re.compile('熱量')).parent.next_sibling.next_sibling.text
                        calories_dic[store_name][product_name] = float(product_calories.strip("kcal大卡 "))
                    except:
                        pass
            if 110 < count:
                try:
                    product_calories = product_soup.find('th', string=re.compile('熱量')).next_sibling.next_sibling.text
                    calories_dic[store_name][product_name] = float(product_calories.strip(strip))
                except:
                    pass

print(calories_dic)          
