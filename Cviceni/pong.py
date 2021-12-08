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
VELIKOST_FONTU = 42
ODSAZENI_TEXT = 30

# Dále nadefinujeme proměnné
pozice_palek = [VYSKA // 2, VYSKA // 2] # vertikální pozice dvou pálek
pozice_mice = [0, 0] # x, y souřadnice míčku - nastavené v reset()
rychlost_mice = [0, 0] #x, y složky rychlosti míčku - nastavené v reset()
stisknute_klavesy = set() # sada stisknutých kláves
skore = [0, 0] # skore dvou hráčů

from pyglet import gl

def vykresli_obdelnik(x1, y1, x2, y2):
    """Nakresli obdelnik na dane souradnice

    Nazorny diagram::

         y2 - +-----+
              |/////|
         y1 - +-----+
              :     :
             x1    x2
    """  
    # Tady použijeme volání OpenGL, které je pro nás zatím asi nejjednodušši na použití
    gl.glBegin(gl.GL_TRIANGLE_FAN) # začni kreslit spojené trojúhelníky
    gl.glVertex2f(int(x1), int(y1)) # vrchol A
    gl.glVertex2f(int(x1), int(y2)) # vrchol B
    gl.glVertex2f(int(x2), int(y2)) # vrchol C, nakresli trojúhelník ABC
    gl.glVertex2f(int(x2), int(y1)) # vrchol D, nakresli trojúhelník BCD
    # další souřadnice E by nakreslila trojúhelník CDE, atd.
    gl.glEnd() # ukončí kreslení trojúhelníků

import pyglet

def vykresli():
    ''' Vykreslí stav hry'''
    gl.glClear(gl.GL_COLOR_BUFFER_BIT) # smaž obsah okna (vybarvi na černo)
    gl.glColor3f(1, 1, 1) # nastav barvu kreslení na bílou
    # vykreslení míčku
    vykresli_obdelnik(
        pozice_mice[0] - VELIKOST_MICE // 2,
        pozice_mice[1] - VELIKOST_MICE // 2,
        pozice_mice[0] + VELIKOST_MICE // 2,
        pozice_mice[1] + VELIKOST_MICE // 2,
    )
    # vykreslení pálky vlevo
    vykresli_obdelnik(
        0,
        pozice_palek[0] - DELKA_PALKY // 2,
        TLOUSTKA_PALKY,
        pozice_palek[0] + DELKA_PALKY // 2,
    )
    # vykreslení pálky vpravo
    vykresli_obdelnik(
        SIRKA - TLOUSTKA_PALKY,
        pozice_palek[1] - DELKA_PALKY // 2,
        SIRKA,
        pozice_palek[1] + DELKA_PALKY // 2,
    )

window = pyglet.window.Window(width = SIRKA, height = VYSKA)
window.push_handlers(
    on_draw = vykresli, #na vykreslení okna použij funkci 'vykresli'
)

pyglet.app.run() # vše je nastaveno, ať začně hra!