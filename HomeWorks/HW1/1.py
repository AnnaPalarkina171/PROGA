import random
import re

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
        
    with open(name, encoding='utf-8') as f:
        text = f.read()
        word = random.choice(text.split())
        print(word)
    return word

def trying(word):
    hint = ['_ ']*len(word)
    for num_try in range(13,0,-1):  
        if num_try <= 1:
            tries = 'У Вас есть {} попытка угадать слово из {} букв  '.format(num_try,len(word))
        if 5 > num_try > 1:
            tries = 'У Вас есть {} попытки угадать слово из {} букв  '.format(num_try,len(word))
        if num_try >= 5:
            tries = 'У Вас есть {} попыток угадать слово из {} букв  '.format(num_try,len(word))
        print(tries,*hint)

        given_letter = input('Угадайте одну букву: ')
        if given_letter != '':
            
            if given_letter in word.lower():
                with open('congrads.txt',encoding='utf-8') as f:
                    text = f.read()
                    congrads = random.choice(text.splitlines())
                    print(congrads,'\n')
                    
            if given_letter not in word.lower():
                with open('wrong.txt', encoding='utf-8') as f:
                    text = f.read()
                    wrong = random.choice(text.splitlines())
                    print(wrong,'\n')

            rus_letter = re.findall(r'[а-яА-Я]', given_letter)      
            
            #print('Необходимо ввести русскую букву')
                
            
        else:
            with open('empty.txt', encoding='utf-8') as f:
                    text = f.read()
                    empty = random.choice(text.splitlines())
                    print(empty,'\n')
        
        num=0
        for word_letter in word.lower():
            num+=1
            if given_letter == word_letter:
                hint[num-1] = given_letter
        


  

def main():
    trying(topic())

main()

     


        
