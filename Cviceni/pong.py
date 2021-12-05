# Nadefinujeme si nejdříve konstanty pro herní obrazovku
# Konstanty značíme verzálkami
# Velikost okna (v pixelech)
SIRKA = 900
VYSKA = 600

VELIKOST_MICE = 20
TLOUSTKA_PALKY = 10
DELKA_PALKY = 100
RYCHLOST = 200 # V pixelech za sekundu
RYCHLOST_PALKY = RYCHLOST * 1.5 # taky v pixelech za sekundu

SIRKA_PULICI_CARKY = 20
VELIOST_FONTU = 42
ODSAZENI_TEXT = 30


# Dále nadefinujeme proměnné
pozice_palek = [VYSKA // 2, VYSKA // 2] # vertikální pozice dvou pálek
pozice_mice = [0, 0] # x, y souřadnice míčku - nastavené v reset()
rychlost_mice = [0, 0] #x, y složky rychlosti míčku - nastavené v reset()
stisknute_klavesy = set() # sada stisknutých kláves
skore = [0, 0] # skore dvou hráčů

import pyglet

window = pyglet.window.Window(width = SIRKA, height = VYSKA)
pyglet.app.run()
