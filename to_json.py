import json

li = []
with open('blacklist.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            li.append(n)

with open('blacklist.json', 'w', encoding='utf-8') as k:
    json.dump(li, k)
