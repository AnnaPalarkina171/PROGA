import os
import re
import requests
import html
from bs4 import BeautifulSoup
import sqlite3

links = []
data = []
titles = []


def title_data_link():
    for i in range(1,2):
        url = 'http://pav-edin23.ru/category/obshhestvo/page/' + str(i) + '/'
        r = requests.get(url)
        text = r.text
        soup = BeautifulSoup(text, 'html.parser')
        divs = soup.findAll('div', {'class': 'entry-thumb'})
        for div in divs:
            for anchor in div.find_all('a'):
                a = anchor.get('href')
                links.append(a)
                dat = re.compile(r'[\d{4}/\d{2}/\d{2}]')
                dat = dat.findall(a)
                year = ''.join(dat[5:9])
                month = ''.join(dat[10:12])
                day = ''.join(dat[13:15])
                dat = year +'.'+ month +'.'+ day
                data.append(dat)
                title = a.split('/')[-2]
                titles.append(title)

def text():
    for link in links:
        r = requests.get(link)
        text = r.text
        soup = BeautifulSoup(text, 'html.parser')
        regTag = re.compile('<.*?>', re.DOTALL)
        regScript = re.compile('<script>.*?</script>', re.DOTALL)
        regComment = re.compile('<!--.*?-->', re.DOTALL)
        regNum = re.compile(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?')
        regLang = re.compile(r'[^ЁА-Яёа-я ]')
        divs = soup.findAll('div', {'class': 'entry entry-content'})
        for div in divs:
            p = div.findAll('p')
            clean_p = regScript.sub("", str(p))
            clean_p = regComment.sub("", clean_p)
            clean_p = regTag.sub("", clean_p)
            pure_text = clean_p                                         #обычный текст для БД
            clean_p = html.unescape(clean_p)
            clean_p = regNum.sub("", clean_p)
            clean_p = regLang.sub("", clean_p)                         #чистый текст для mystem

            path = os.getcwd()
            lin = link.split('/')[-2]
            name1 = path + '\\' + 'book' + '\\' + lin[0:10] + '.txt'
            name2 = path + '\\' + 'book' + '\\' + lin[0:10] + '.xml'                        #лемматезированные тексты
            with open(name1, 'w', encoding='utf-') as f:
                f.write(clean_p)
            os.system(r'C:\\Users\\User\\Desktop\\mystem.exe -cdgin  --eng-gr {} {}'.format(name1, name2))

def table():
    path = os.getcwd()
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE project (title text, data text, link text, text text, mystem text) """)
    for index in range(len(links)):
        line = []
        tup = ()
        lin = links[index].split('/')[-2]
        name1 = path + '\\' + 'book' + '\\' + lin[0:10] + '.txt'
        name2 = path + '\\' + 'book' + '\\' + lin[0:10] + '.xml'
        with open(name1, 'r', encoding='utf-8') as f:
            text = f.read()
        with open(name2, 'r', encoding='utf-8') as t:
            mystem = t.read()
        tup = (titles[index], data[index], links[index], text, mystem)
        line.append(tup)
        cursor.executemany("INSERT INTO project VALUES (?,?,?,?,?)", line)
        conn.commit()







title_data_link()
text()
table()




