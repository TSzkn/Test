#获取缩写对应的中文
import json
import time

import requests
from bs4 import BeautifulSoup

def getName(MoneyName):
    currency_mapping = {}
    url = "https://www.11meigui.com/tools/currency"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('td', id='desc')

        child_tables = table.find_all('table')
        for table in child_tables:

            trList = table.find_all('tr')
            for row in trList[2:]:  # 跳过表头行
                cols = row.find_all('td')
                print(cols)
                #time.sleep(1)
                currency_name = cols[1].text.strip()
                currency_code = cols[4].text.strip()
                currency_mapping[currency_name] = currency_code
    print(currency_mapping)
    for key, val in currency_mapping.items():
        if val == MoneyName:
            return key

# output_file = "currency_data.json"
# with open(output_file, 'w') as file:
#     json.dump(currency_mapping, file, ensure_ascii=False, indent=4)


