from bs4 import BeautifulSoup
import requests
import re

url='https://rozklad.ztu.edu.ua/schedule/group/ІПЗ-21-1'

response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
tabels = soup.find('div', style='margin:0 20px;').find_all('table', class_="schedule")


def scheldule_parse(entities, condition):
    auditories = {}
    for table in entities:
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
                                if condition in div.text:
                                    if not div.find('div',class_='one'):
                                        aud = re.findall('\d+', div.find('span').text.strip())[0]
                                        if aud in auditories:
                                            auditories[aud] += 1
                                        else:
                                            auditories[aud] = 1
        return auditories


if __name__=='__main__':
    print('Most often in lab aud:')
    result = scheldule_parse(tabels,'Лабораторна,ауд.')
    max_a=max(list(result.values()))

    for i,x in result.items():
        if x==max_a:
            print(F"Lab aud N{i} - {x} lessons")
            break