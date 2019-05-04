import urllib.request
import json
from datetime import datetime
import sqlite3
import time
import os
import re
from pymystem3 import Mystem

mystem = Mystem()

token = '4cfa74c198e70aeba8ade125e944e4505e31bdf682cca525d9e32abb669a682a92169c8db2524d1f9e4da'
group = 'team'
owner_id = '-22822305'
method_wall = 'wall.get?'
method_comments = 'wall.getComments?'


def request(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    data = json.loads(result)
    return data


def write(text_for_corpus):
    with open('corpus\plain_texts.txt', 'a', encoding='utf-8') as f:
        f.write(text_for_corpus)
        f.write(' ')


def lemmatizer():
    plain = 'C:\\Users\\User\\Desktop\\PROGA\\HomeWorks\\HW6\\corpus\\plain_texts.txt'
    mystem = 'C:\\Users\\User\\Desktop\\PROGA\\HomeWorks\\HW6\\corpus\\mystem_texts.xml'
    os.system(r'C:\\Users\\User\\Desktop\\mystem.exe -cdgin --format xml --eng-gr {} {}'.format(plain, mystem))
    with open('C:\\Users\\User\\Desktop\\PROGA\\HomeWorks\\HW6\\corpus\\mystem_texts.xml', 'r', encoding='utf-8') as f:
        text = f.read()
        list_words = re.findall(r'lex="(.*?)"', text)
        with open('corpus\lemmatized_texts.txt', 'w', encoding='utf-8') as f:
            f.write(' '.join(list_words))


post_text = []  # ТЕКСТ ПОСТА
post_id = []  # ID ПОСТА
post_year = []  # ГОД ПОСТА
post_month = []  # МЕСЯЦ ПОСТА
post_lemmatized = []  # ЛЕММАТИЗИРОВАННЫЕ ТЕКСТЫ ПОСТА
post_len = []  # ДЛИНА ПОСТА В СЛОВАХ

# ПОСТЫ
url = 'https://api.vk.com/method/wall.get?owner_id=-22822305&count=10&v=5.92&access_token=%s' % (token)
data = request(url)
text = data['response']['items']
for x in text:
    if x['text'] == '':
        dic = x['copy_history']
        post_text.append(dic[0]['text'])
        txt = dic[0]['text']
        txt = re.sub(r'\n', r' ', txt)
        txt = re.sub(r'[^а-яА-ЯёЁ ]', '', txt)
        txt = re.sub(r'   ', r' ', txt)
        text_lem = [text for text in mystem.lemmatize(txt)]
        post_lemmatized.append(''.join(text_lem))
        post_len.append(len(text_lem))
    else:
        txt = x['text']
        txt = re.sub(r'\n', r' ', txt)
        txt = re.sub(r'[^а-яА-ЯёЁ ]', '', txt)
        txt = re.sub(r'   ', r' ', txt)
        text_lem = [text for text in mystem.lemmatize(txt)]
        post_lemmatized.append(''.join(text_lem))
        post_len.append(len(text_lem))
        post_text.append(x['text'])
    post_id.append(x['id'])
    time_post = x['date']
    utc = datetime.fromtimestamp(time_post)
    post_year.append(str(utc).split('-')[0])
    post_month.append(str(utc).split('-')[1])

# КОММЕНТАРИИ
post_id_com = []  # ID ПОСТЕ КАЖДОГО КОММЕНТА
com_text = []  # ТЕКСТ КОММЕНТА
com_id = []  # ID КОММЕНТА
com_lemmatized = []  # ЛЕММАТИЗИРОВАННЫЕ ТЕКСТЫ КОММЕНТА
com_len = []  # ДЛИНА КОММЕНТА В СЛОВАХ
from_id = []  # ID КОММЕНТАТОРА
cities = []  # ГОРОДА КОММЕНТАТОРОВ
sex_com = []  # ПОЛ КОММЕНТАТОРА

token = '32e55c8bd2d2f1416ee24b3650570d047a6f9daeae48985c2867921a05e507ed169db43e3d696a20f97c3'

for pst_id in post_id:
    time.sleep(2)
    url = 'https://api.vk.com/method/wall.getComments?owner_id=-22822305&post_id=%s&count=10&v=5.92&access_token=%s' % (
    pst_id, token)
    data = request(url)
    text = data['response']['items']
    for x in text:
        if 'deleted' not in x.keys():
            post_id_com.append(x['post_id'])  # ID ПОСТА
            com_text.append(x['text'])  # ТЕКСТ КОММЕНТА
            com_id.append(x['id'])  # ID КОММЕНТА
            from_id.append(x['from_id'])  # ID КОММЕНТАТОРА
            txt = x['text']
            txt = re.sub(r'\n', r' ', txt)
            txt = re.sub(r'[^а-яА-ЯёЁ ]', '', txt)
            txt = re.sub(r'   ', r' ', txt)
            text_lem = [text for text in mystem.lemmatize(txt)]
            com_lemmatized.append(''.join(text_lem))
            com_len.append(len(text_lem))

token = 'c448a53152f68390ba28798534e45f44a851148dfe48056385fc31c0beb24b43f3973a7eef0cc0bd278eb'



print(*from_id)





for id_com in from_id:
    time.sleep(5)
    url = 'https://api.vk.com/method/users.get?v=5.92&access_token=%s&fields=city&user_ids=%s' % (token, id_com)
    data = request(url)
    print(data)
    if 'city' not in (data['response'][0].keys()):
        cities.append('none')
    else:
        city = data['response'][0]['city']
        cities.append(city['title'])

token = 'ac699d06904730fd8d754fc9dcc5d7bb46f4e3d52ed1741670e2fe467bb281f1ffa926ac62d72c664269f'

for id_com in from_id:
    time.sleep(5)
    url = 'https://api.vk.com/method/users.get?v=5.92&access_token=%s&fields=sex&user_ids=%s' % (token, id_com)
    data = request(url)
    if 'sex' not in (data['response'][0].keys()):
        sex_com.append('none')
    else:
        sex = data['response'][0]['sex']
        if sex == 1:
            sex_com.append('female')
        if sex == 2:
            sex_com.append('male')

# СТРОИМ БАЗУ ДАННЫХ - 2 таблицы в одной базе - для поста и для комментов
conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS comments(post id, comment id, person id, text, lemmas, len, city, sex)")
for i in range(len(com_id)):
    lst = []
    lst.append(post_id_com[i])
    lst.append(com_id[i])
    lst.append(from_id[i])
    lst.append(com_text[i])
    lst.append(com_lemmatized[i])
    lst.append(com_len[i])
    lst.append(city[i])
    lst.append(sex_com[i])
    c.execute('INSERT INTO comments VALUES (?, ?, ?, ?, ?, ?, ?, ?)', lst)
    conn.commit()

c.execute("CREATE TABLE IF NOT EXISTS posts(id, text, lemmas, len, year, month)")
for i in range(len(post_id)):
    lst = []
    lst.append(post_id[i])
    lst.append(post_text[i])
    lst.append(post_lemmatized[i])
    lst.append(post_len[i])
    lst.append(post_year[i])
    lst.append(post_month[i])
    c.execute('INSERT INTO posts VALUES (?, ?, ?, ?, ?, ?)', lst)
    conn.commit()

#ДЕЛАЕМ КОРПУС
for text in post_text:
    text_for_corpus = text
    write(text_for_corpus)
for text in com_text:
    text_for_corpus = text
    write(text_for_corpus)

lemmatizer()