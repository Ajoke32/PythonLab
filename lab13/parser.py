from bs4 import BeautifulSoup
import requests
import re
from my_group import scheldule_parse

url='https://rozklad.ztu.edu.ua/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')


head =soup.find_all('div',class_='container')
fikt_div=''

for i in head:
    next_div=i.find('div',class_='row auto-clear')
    if next_div:
        div_with_h4=next_div.find('div',class_='col l12 s12')
        if div_with_h4:
            h4 = div_with_h4.find('h4')
            if h4.text=='Факультет інформаційно-комп\'ютерних технологій':
                fikt_div=next_div
                break

fikt_collection_wraps = fikt_div.find_all('div',class_='col l2 s6 m4')


def get_frequency(where:str):
    auditories = {}
    for wrap in fikt_collection_wraps:
        collecs = wrap.find_all('div',class_='collection')
        for col in collecs:
            links =col.find_all('a')
            for a in links:
                shd_respone = requests.get(url + a['href'])
                shd_soup = BeautifulSoup(shd_respone.text, 'lxml')
                tabels = shd_soup.find('div', style='margin:0 20px;').find_all('table', class_="schedule")
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
                                            if where in div.text:
                                                if not div.find('div', class_='one'):
                                                    aud = re.findall('\d+', div.find('span').text.strip())[0]
                                                    if aud in auditories:
                                                        auditories[aud] += 1
                                                    else:
                                                        auditories[aud] = 1
    return auditories




if __name__=="__main__":

    lect = get_frequency('Лекція,ауд.')
    sort_lect = sorted(lect.items(), key=lambda x: x[1], reverse=True)
    print("Top 5 lect aud:")
    
    for i in range(0,4):
        print(F"Lecture room N{sort_lect[i][0]} - {sort_lect[i][1]} lessons")

    """
    ті практичні аудиторії, що наймейше застосовуються - менше всього задіяні за весь час
    тей самий пошук тільки пошук практичних
    """

    prakt = get_frequency('Лабораторна,ауд.')
    sort_prakt = sorted(prakt.items(), key=lambda x: x[1])
    print("Top 5 min lab:")
    for i in range(0,4):
        print(F"Lab room N{sort_prakt[i][0]} - {sort_prakt[i][1]} lessons")
