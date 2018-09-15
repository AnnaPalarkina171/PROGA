import random
#скачать pay charms - адаптор для питона
Number_of_tries = 5

def theme():
    theme_asking = input ('если вы хотите выбрать тему 1, введите 1: ')
    if theme_asking == '1':
        file = 'terms_ling.txt' #если пользователь ввел 1, то программа берет файл 1
    elif theme_asking == '2':
        file = 'terms_math.txt'
    else:
        file = 'terms_names.txt'
    return file


def open_file():
    file = theme()
    with open (file, encoding = 'utf-8') as f:
        words = f.read().lower()
    words = words.split('\n') #теперь текст - отдельные слова
    word = random.choice(words)
    return word


def working_with_word(word): #обрабатываем слово
    unknown_word = ['_' for i in range(len(word))]
    print (' '.join(unknown_word)) #на выходе теперь строка, а не список (убрались кавычки)
    return unknown_word


def letters (uknown_word, word):
    letter = input('Введите букву: ').lower()
    if letter in word:
        for i in range (len(word)):       #сравниваем букву с каждым элементом
            if letter == word (i):
                unknown_word[i] = letter
                
        print('Поздравляем, вы угадали букву!')
        print (' '.join(unknown_word))
    else:
        print ('Вы не угадали букву')
        global Number_of_tries
        Number_of_tries = Number_of_tries - 1
        print ('Количество оставшихся попыток: {} '.format{Number_of_tries})
            
                       
            
def main():
    word = open_file()
    print(word) 
    working_with_word(word)
    unknown_word = working_with_word()
    letters(unknown_word, word)

main()
    



    
    
            
