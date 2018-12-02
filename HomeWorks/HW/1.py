colors = ["coral", "aqua", "blueviolet", "deepskyblue", "hotpink", "blue", "chartreuse", "tomato", "brown"]
data = {}
gend = {}
col = {}
with open('names.csv', 'r', encoding='utf-8') as n:
    n = n.read()
    names = n.split(',')
    names.remove('')
    for name in names:
        nam = name.split('\\')
        nam = nam[-1]
        nam = nam.split('.')
        language = nam[0]
        gender = nam[1]
        with open(name, 'r', encoding='utf-8') as f:
            content = f.read().split('\n')
            content.remove('')
            for a in content:
                a = a.split(',')
                for num in range(9):
                    data[language] = gend
                    gend[gender] = col
                    col[colors[num]] = a[num]
                   
                   

print(data)                    
                
