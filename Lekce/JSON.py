# Existuje modul json, jehož metoda loads načte data z řetězce:
import json

json_retezec = '''
    {
        "jméno": "Anna",
        "město": "Brno",
        "jazyky": ["čeština", "angličtina", "Python"],
        "věk": 26
    }
'''

data = json.loads(json_retezec)
print(data)
print(data["město"])

# Metoda dumps, která naopak daná data zakóduje a vrátí řetězec:
print(json.dumps(data))

# Má-li výsledná data číst člověk, nastav ensure_ascii=False (aby se písmenka s diakritikou nekódovala pomocí \) a indent=2 (odsazení dvěma mezerami)
print(json.dumps(data, ensure_ascii=False, indent=2))
