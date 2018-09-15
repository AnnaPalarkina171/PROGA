import random

letters  = ['a','b','c','d','e','f','g','h','i',
            'j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z']
let = random.choice(letters)

a = input('Угадайте английскую букву, оторую я загадал: ')

if let != a:
        ind_a = letters.index(a)
        ind_x = letters.index(let)
        if ind_a > ind_x:
            print('Левее')
        if ind_a < ind_x:
            print('Правее')

else:
    print('Верно!') 
   




        





