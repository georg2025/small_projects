# Задача была собрать данные по всем компаниям, у которых имеются лицензии на сбор отходов 1-4 класса опасности. В реальности я использовал 3 представленных тут парсера отдельно.
# Здесь впихнул все в одну кучу, чтобы нагляднее было. Сейчас на сайте РПН все поменяли, так что, вряд ли он будет работать.

import requests
from bs4 import BeautifulSoup as BS
import time
import random
import re

x = open('Коды_url.txt', 'w')
count = 1
HEADERS = {
    # Здесь нужно написать заголовок HTTP конкретно вашего компа. Можно, в принципе, ничего не писать.

}


def parser():
    response = requests.get(url, headers=HEADERS)
    soup = BS(response.content, "html.parser")
    data = soup.select("a")
    for i in data:
        z=i.attrs["href"]
        if len(z)==18:
            f=z[10:17]
            x.write(f + '\n')
            print(f)

for t in range(1, 2):
    q=str(t)
    url = "https://rpn.gov.ru/licences/?name=&hazard_class=&region=%D0%92%D1%81%D0%B5&types=&inn=&org=&status=%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%88%D0%B0%D1%8F&page=page-"+q
    parser()
    time.sleep(1)


n = 1

adresses = []

file=open("Коды_url.txt")

while True:
    w=file.readline()
    if not w: break
    adresses.append(w.rstrip())

file2=open("OGRN.txt", "w")

def parser1():
    try:
        l = 1
        response = requests.get(url, headers=HEADERS)
        soup = BS(response.content, "html.parser")
        data = soup.findAll("p", class_="registryCard__listContent _medium")
    # print(data)
        for items in data:
            try:
                if l == 6:
                    item = items.get_text(strip=True)
                    file2.write(item + '\n')
                    print(item)
                    l += 1
                else:
                    l += 1
            except Exception as ex:
                print ("супер ошибка")
                pass
    except Exception as ex:
        print ("ошибка")
        pass

for q in adresses:
    url = "https://rpn.gov.ru/licences/" + q + "/"
    parser1()
    print(str(n))
    n += 1
    #time.sleep(2)

def parser2():
    try:
        response = requests.get(url, headers=HEADERS)
        soup = BS(response.content, "html.parser")
        data = soup.findAll("a", class_="link", rel='nofollow')
        for items in data:
            item = items.get_text(strip=True)
            item2 = re.findall(r'@', item)
            if item2 == ['@']:
                file4.write(item + '\n')
                print(item)
            else:
                pass
    except Exception as ex:
        print ("ошибка")
        pass

adresses = set()

file3=open("OGRN.txt")

while True:
    w=file3.readline()
    if not w: break
    adresses.add(w.rstrip())

file4=open("Adresses.txt", "w")

for q in adresses:
    url = "https://checko.ru/company/" + q
    parser2()
    count+=1
    print(str(count))
    time.sleep(random.randint(3,5))



