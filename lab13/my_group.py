from bs4 import BeautifulSoup
import requests
import re

url='https://rozklad.ztu.edu.ua/schedule/group/ІПЗ-21-1'

response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
tabels = soup.find('div', style='margin:0 20px;').find_all('table', class_="schedule")

auditories={}

for table in tabels:
    trs = table.find_all('tr')
    for y in trs:
        td = y.find_all('td', class_='content')
        if td:
            for t in td:
                var_div = t.find('div', class_='variative')
                if var_div:
                    subg_div = var_div.find_all('div')
                    if subg_div:
                        for div in subg_div:
                            if 'Лабораторна,ауд.' in div.text:
                                aud = re.findall('\d+', div.find('span').text.strip())[0]
                                if aud in auditories:
                                    auditories[aud] += 1
                                else:
                                    auditories[aud] = 1

print('Most often in lab aud:')
max_a=max(list(auditories.values()))

for i,x in auditories.items():
    if x==max_a:
        print(F"Lab aud N{i} - {x} lessons")
        break