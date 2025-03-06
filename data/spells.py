import requests

# a = requests.get('https://hp-api.onrender.com/api/spells')
a = requests.get('https://potterhead-api.vercel.app/api/spells')


with open('spells2.txt', 'w') as f:
    for i in range(len(a.json())):
        f.write(a.json()[i]["name"] + ',' + a.json()[i]["description"] + "\n")

print("DONE")