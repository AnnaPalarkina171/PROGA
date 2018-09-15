import random
import re

#выбираем 1 тему игры из 3х предложенных
def topic():
    topic = input("""Сейчас мы будем играть в 'Виселицу'. Вам нужно выбрать одну из предложенных тем.
                 Нажмите 1, если хотите угадывать лингвистические термины
                 Нажмите 2, если хотите угадывать математические термины
                 Нажмите 3, если хотите угадывать фамилии известных лингвистов
                 Ваш выбор: """)

    if topic == '1':
        name = 'terms_ling.txt'       
    if topic == '2':
        name = 'terms_math.txt'
    if topic == '3':
        name = 'terms_names.txt'
    return name

#рандомно выбираем слово из предложенной темы
def word(name):
    with open(name, encoding='utf-8') as f:
        text = f.read()
        word = random.choice(text.split())
        print(word)
    return word

def 

word(topic())




















