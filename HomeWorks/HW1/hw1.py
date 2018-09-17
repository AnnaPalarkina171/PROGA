import random
import re

man = [
    '''

          |
          |
          |
          |
          |
  =========''',
    '''
  
          +
          |
          |
          |
          |
          |
  =========''',
    '''
  
         -+
          |
          |
          |
          |
          |
  =========''',
    '''
  
        --+
          |
          |
          |
          |
          |
  =========''',
    '''
  
       ---+
          |
          |
          |
          |
          |
  =========''',
    '''
  
      +---+
          |
          |
          |
          |
          |
  =========''',
    '''
  
      +---+
      |   |
          |
          |
          |
          |
  =========''',
    '''
  
      +---+
      |   |
      0   |
          |
          |
          |
  =========''',
     '''
  
      +---+
      |   |
      0   |
      |   |
          |
          |
  =========''',
     '''
  
      +---+
      |   |
      0   |
     /|   |
          |
          |
  =========''',
    '''
  
      +---+
      |   |
      0   |
     /|\  |
          |
          |
  =========''',
    '''
  
      +---+
      |   |
      0   |
     /|\  |
     /    |
          |
  =========''',
    '''
  
      +---+
      |   |
      0   |
     /|\  |
     / \  |
          |
  =========''',
    ]


#выбираем 1 тему игры из 3х предложенных
def topic123():
    topic = input("""Сейчас мы будем играть в 'Виселицу'. Вам нужно выбрать одну из предложенных тем.
                 Нажмите 1, если хотите угадывать лингвистические термины
                 Нажмите 2, если хотите угадывать математические термины
                 Нажмите 3, если хотите угадывать физические термины
                 Ваш выбор: """)

    if topic == '1':
        name = 'terms_ling.txt'       
    if topic == '2':
        name = 'terms_math.txt'
    if topic == '3':
        name = 'terms_physics.txt'
    if topic == '':
        print('Вы ничего не ввели')
        topic123() 
    return name


#рандомно выбираем слово из предложенной темы
def word():
    name = topic123()
    with open(name, encoding='utf-8') as f:
        text = f.read()
        random_word = random.choice(text.split())
    return random_word


#пишем число попыток и подсказку
def trying(random_word):
    dying = 0
    word_list = []
    #for letter in random_word:
        #word_list.append(letter)
    hint = ['_ ']*len(random_word)
    for num_try in range(12,-1,-1):
        if hint == word_list:
            print('Вы выиграли!')
            break
        if num_try == 1:
            tries = 'У Вас есть {} попытка угадать слово из {} букв  '.format(num_try,len(random_word))
        if 5 > num_try > 1:
            tries = 'У Вас есть {} попытки угадать слово из {} букв  '.format(num_try,len(random_word))
        if num_try >= 5:
            tries = 'У Вас есть {} попыток угадать слово из {} букв  '.format(num_try,len(random_word))
        if num_try == 0:
            print('К сожалению, попытки закончились. Вы проиграли(', 'Загаданное слово: ', random_word)
            print(man[12])
            break
        print(tries, *hint)
     
        #игрок вводит букву
        given_letter = input('Угадайте одну букву: ')
        given_letter = given_letter.lower()
        num=0
        if  given_letter in hint:
            with open('again.txt', encoding='utf-8') as f:
                text = f.read()
                again = random.choice(text.splitlines())
                print(again,'\n')
                dying+=1
                print(man[dying])
        if given_letter not in hint:                     
            for random_word_letter in random_word:
                word_list.append(random_word_letter)
                num+=1  
                #если буква угадана, меняем подсказку
                if given_letter == random_word_letter:
                    hint[num-1] = given_letter
                
            #проверяем input() на соответствие одной русской букве         
            if len(given_letter) > 1:
                print('Необходимо ввести только одну букву','\n')
                dying+=1
                print(man[dying])
            else:   
                if given_letter !=  '':
                    if not re.findall(r'[а-яёА-ЯЁ]',given_letter):
                        print('Необходимо ввести рускую букву', '\n')
                        dying+=1
                        print(man[dying])
                    else:
                        if given_letter in random_word:  
                            with open('congrads.txt',encoding='utf-8') as f:                                                                                                                
                                text = f.read()
                                congrads = random.choice(text.splitlines())
                                print(congrads)
                                print(man[dying])
       
                        if given_letter not in random_word:
                            with open('wrong.txt', encoding='utf-8') as f:
                                text = f.read()
                                wrong = random.choice(text.splitlines())
                                print(wrong,'\n')
                                dying+=1
                                print(man[dying])
                    
                if given_letter == '':
                    with open('empty.txt', encoding='utf-8') as f:
                        text = f.read()
                        empty = random.choice(text.splitlines())
                        print(empty,'\n')
                        dying+=1
                        print(man[dying])
                
def main():
    random_word = word()
    trying(random_word)
main()




