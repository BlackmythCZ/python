import requests
# stažení stránky
stranka = requests.get('https://github.com')

# ověření, že dotaz doběhl v pořádku
stranka.raise_for_status()

# vypsání obsahu stránky
print(stranka.text)

with open('D:\\Git\\python\\Hesla\\token.txt') as soubor:
    token = soubor.read().strip()

headers = {'Authorization': 'token ' + token}

stranka = requests.get('https://api.github.com/user', headers=headers)
stranka.raise_for_status()
print(stranka.text)

# převedení výpisu stránky z JSON na slovník a srozumitelnější výpis
import json 
data = json.loads(stranka.text)
print(json.dumps(data, ensure_ascii=True, indent=2))
print(data['avatar_url'])

# Úpravy obsahu přes API - ohvězdičkování obsahu repo
with open('D:\\Git\\python\\Hesla\\token.txt') as soubor:
    token = soubor.read().strip()

headers = {'Authorization': 'token ' + token}

stranka = requests.put('https://api.github.com/user/starred/BlackmythCZ/python', headers=headers)
stranka.raise_for_status()