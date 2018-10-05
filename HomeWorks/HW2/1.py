import json
import urllib.request
from collections import Counter
#users = ['elmiram', 'maryszmary', 'lizaku', 'nevmenandr', 'ancatmara', 'roctbb', 'akutuzov', 'agricolamz', 'lehkost','kylepjohnson',
         #'mikekestemont', 'demidovakatya', 'shwars', 'JelteF', 'timgraham', 'arogozhnikov', 'jasny', 'bcongdon', 'whyisjake']

users = ['lizaku', 'elmiram', 'maryszmary'] #список такой маленький, потому что иначе все ломается(((

#User choses one username from the given list and gets name and description of each repositories
def username():
    print('Usernames: ')
    for user in users:
        print('{}{}'.format('\t',user))
    user_name = input('Chose one of the following usersnames: ')
    while user_name not in users:
        print('Wrong username! Select one of the options!')
        user_name = input('Chose one of the following usersnames: ')
    if user_name in users:
        token = '0376e2ecd95fdf6057082bae159df943ee91e538'
        url = 'https://api.github.com/users/%s/repos?access_token=%s' %(user_name,token)
        reponse = urllib.request.urlopen(url)
        text = reponse.read().decode('utf-8')
        data = json.loads(text)
        print('User {} has {} repositories\n'.format( user_name,len(data)))
        num = 1
        for item in data:
            name = item['name']
            description = item['description']
            print(num, 'Name: {}\n Description: {}\n'.format(name, description))
            num += 1
    return data
        
#The list of languages and numbers of repositories where each language was used
def languages_one_user(data):     
    languages = []
    for item in data:
        languages.append(item['language'])
    c = Counter(languages)
    for key, value in c.items():
        if key != None:
            print('{} is used in {} repositories'.format(key, value))
    print('\n')
        
#The list of repositories of each user and the name of user with the largest number of repositories        
def big_repos():
    names = []
    lens = []
    for user in users:
        token = '0376e2ecd95fdf6057082bae159df943ee91e538'
        url = 'https://api.github.com/users/%s/repos?acces_token=%s' %(user, token)
        reponse = urllib.request.urlopen(url)
        text = reponse.read().decode('utf-8')
        data = json.loads(text)
        names.append(user)
        lens.append(len(data))
    dict_repos = dict(zip(names,lens))
    for key, value in dict_repos.items():
        print('User {} has {} repositories'.format(key, value))
        if value == max(lens):
            max_name = key
            max_num = value
    print('\nUser {} has the largest number of repositories: {}\n'.format(max_name, max_num))

#The most popular language among the following users
def languages():
    languages = []
    for user in users:
        token = '0376e2ecd95fdf6057082bae159df943ee91e538'
        url = 'https://api.github.com/users/%s/repos?acces_token=%s' %(user, token)
        reponse = urllib.request.urlopen(url)
        text = reponse.read().decode('utf-8')
        data = json.loads(text)
        for item in data:
            if item['language'] != None:
                languages.append(item['language'])
    c = Counter(languages)
    most_common_lang = c.most_common(1)
    for key, value in most_common_lang:
        print('{} is the most common language. It ised in {} repositories of {} users'.format(key, value, len(users)))

#User with the largest number of followers
def followers():
    num_followers = []
    name = []
    max_fols = []
    for user in users:
        token = '0376e2ecd95fdf6057082bae159df943ee91e538'
        url = 'https://api.github.com/users/%s/followers?acces_token=%s' %(user, token)
        reponse = urllib.request.urlopen(url)
        text = reponse.read().decode('utf-8')
        data = json.loads(text)
        num_followers.append(len(data))
        name.append(user)
        dict_fols = dict(zip(name, num_followers))
    for key, value in dict_fols.items():
        if value == max(num_followers):
            max_fols.append(key)
    if len(max_fols) > 1:
        print('{} users have the largest number of followers: {}'.format(len(max_fols),max(num_followers)))
        print(*max_fols, sep='\n')
    if len(max_fols) == 1:
        print('\nUser {} has the largest number of followers: {}'.format(*max_fols,max(num_followers)))
    
        
def main():
    data = username()
    languages_one_user(data)
    big_repos()
    languages()
    followers()
    
main()
