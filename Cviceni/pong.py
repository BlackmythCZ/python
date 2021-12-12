# Nadefinujeme si nejdříve konstanty pro herní obrazovku
# Konstanty značíme verzálkami
# Velikost okna (v pixelech)
SIRKA = 900
VYSKA = 600

VELIKOST_MICE = 20
TLOUSTKA_PALKY = 10
DELKA_PALKY = 100
RYCHLOST = 100 # V pixelech za sekundu
RYCHLOST_PALKY = RYCHLOST * 1.5 # taky v pixelech za sekundu

DELKA_PULICI_CARKY = 20
VELIKOST_FONTU = 42
ODSAZENI_TEXT = 30

# Dále nadefinujeme proměnné
pozice_palek = [VYSKA // 2, VYSKA // 2] # vertikální pozice dvou pálek
pozice_mice = [0, 0] # x, y souřadnice míčku - nastavené v reset()
rychlost_mice = [0, 0] #x, y složky rychlosti míčku - nastavené v reset()
stisknute_klavesy = set() # sada stisknutých kláves
skore = [0, 0] # skore dvou hráčů

from os import times
import random
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
    #vykreslí skóre prvního hráče
    nakresli_text(
        str(skore[0]),
        x = ODSAZENI_TEXT,
        y = VYSKA - VELIKOST_FONTU - ODSAZENI_TEXT,
        pozice_x = "left",
    )
    #vykreslí skóre druhého hráče
    nakresli_text(
        str(skore[1]),
        x = SIRKA - ODSAZENI_TEXT,
        y = VYSKA - VELIKOST_FONTU - ODSAZENI_TEXT,
        pozice_x = 'right',
    )


# Nebo alternativně podle návodu:
#    for x, y in [(0, pozice_palek[0]), (SIRKA, pozice_palek[1])]:
#        nakresli_obdelnik(
#            x - TLOUSTKA_PALKY,
#            y - DELKA_PALKY // 2,
#            x + TLOUSTKA_PALKY,
#            y + DELKA_PALKY // 2,
#        )

    # vykresli půlící čáru
    for y in range(DELKA_PULICI_CARKY // 2, VYSKA, DELKA_PULICI_CARKY * 2):
        vykresli_obdelnik(
            SIRKA // 2 - 1,
            y,
            SIRKA // 2 + 1,
            y + DELKA_PULICI_CARKY
        )

def nakresli_text(text, x, y, pozice_x):
    '''
    Nakreslí daný text na danou pozici

    Argument 'pozice_x' může být 'left' nebo 'right', udává na kterou stranu bude text zarovnaný
    '''
    napis = pyglet.text.Label(
        text,
        font_size=VELIKOST_FONTU,
        x = x, y = y, anchor_x = pozice_x
    )
    napis.draw()

from pyglet.window import key
def stisk_klavesy(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.add(('nahoru', 0))
    if symbol == key.S:
        stisknute_klavesy.add(('dolu', 0))
    if symbol == key.UP:
        stisknute_klavesy.add(('nahoru', 1))
    if symbol == key.DOWN:
        stisknute_klavesy.add(('dolu', 1))

def pusteni_klavesy(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.discard(('nahoru', 0))
    if symbol == key.S:
        stisknute_klavesy.discard(('dolu', 0))
    if symbol == key.UP:
        stisknute_klavesy.discard(('nahoru', 1))
    if symbol == key.DOWN:
        stisknute_klavesy.discard(('dolu', 1))

def obnov_stav(dt):
    for cislo_palky in (0, 1):
        # pohyb podle klaves (viz funkce 'stisk_klavesy')
        # Procházíme v cyklu obě pálky a ptáme se, zda je v množině stisknutých kláves n-tice reprezentující pohyb dané pálky nahoru nebo dolů. Když ano, pohneme pálkou v daném směru (přičteme nebo odečteme od vertikální polohy pálky změnu polohy, což je čas od posledního zavolání, který známe, vynásobený rychlostí pálky nastavené v konstantě).
        if ('nahoru', cislo_palky) in stisknute_klavesy:
            pozice_palek[cislo_palky] += RYCHLOST_PALKY * dt
        if ('dolu', cislo_palky) in stisknute_klavesy:
            pozice_palek[cislo_palky] -= RYCHLOST_PALKY * dt
        
        # dolní zarážka - když je pálka příliš dole, nastavíme ji na minimum
        # Pálku malujeme kolem jejího středu, což znamená, že když se pálka přiblíží na na y-ovou pozici DELKA_PALKY / 2, začíná překračovat dolní hranici hracího pole. V tom případě její pozici zafixujeme na nejnižší možné souřadnici. Analogicky to provedeme, když se blíží hornímu okraji.
        if pozice_palek[cislo_palky] < DELKA_PALKY / 2:
            pozice_palek[cislo_palky] = DELKA_PALKY / 2
        if pozice_palek[cislo_palky] > (VYSKA - DELKA_PALKY / 2):
            pozice_palek[cislo_palky] = (VYSKA - DELKA_PALKY / 2)

        # pohyb míčku
        pozice_mice[0] += rychlost_mice[0] * dt
        pozice_mice[1] += rychlost_mice[1] * dt

        # odraz míčku od stěn
        # Jelikož úhel dopadu se rovná úhlu odrazu, stačí otočit znaménko y-ové složky rychlosti.
        if pozice_mice[1] < VELIKOST_MICE // 2:
            rychlost_mice[1] = abs(rychlost_mice[1])
        if pozice_mice[1] > VYSKA - VELIKOST_MICE // 2:
            rychlost_mice[1] = -abs(rychlost_mice[1])
        
        # definice mezí na y-ové ose, kde se musí míček nacházet, aby byl úspěšně odražen – to je mezi horním a dolním koncem pálky:
        palka_min = pozice_mice[1] - VELIKOST_MICE / 2 - DELKA_PALKY / 2
        palka_max = pozice_mice[1] + VELIKOST_MICE / 2 + DELKA_PALKY / 2

        # Nyní když míček narazí do pravé nebo levé stěny se umíme zeptat, zda je pálka na správné pozici a my máme odrazit míček nebo zda hráč prohrál kolo a my máme přičíst jeho soupeři bod a restartovat hru.
        # odražení vlevo
        if pozice_mice[0] < TLOUSTKA_PALKY + VELIKOST_MICE / 2:
            if palka_min < pozice_palek[0] < palka_max:
                # pálka je na správném místě, odrazí míček
                rychlost_mice[0] = abs(rychlost_mice[0])
            else:
                # pálka není na správném místě
                skore[1] += 1
                reset()
        # odražení vpravo
        if pozice_mice[0] > SIRKA - (TLOUSTKA_PALKY - VELIKOST_MICE / 2):
            if palka_min < pozice_palek[1] < palka_max:
                # pálka je na správném místě, odrazí míček
                rychlost_mice[0] = -abs(rychlost_mice[0])
            else:
                skore[0] += 1
                reset()

from random import randint
def reset():
    pozice_mice[0] = SIRKA / 2
    pozice_mice[1] = VYSKA / 2

    # x-ová rychlost - buď vpravo, nebo vlevo
    if randint(0, 1):
        rychlost_mice[0] = RYCHLOST
    else:
        rychlost_mice[0] = -RYCHLOST
    
    rychlost_mice[1] = random.uniform(-1, 1) * RYCHLOST

# nastaví výchozí stav pro start hry
reset()

window = pyglet.window.Window(width = SIRKA, height = VYSKA)
window.push_handlers(
    on_draw = vykresli, # na vykreslení okna použij funkci 'vykresli'
    on_key_press = stisk_klavesy, # na stisk klávesy provede
    on_key_release = pusteni_klavesy, # na uvolnění klávesy provede
)
pyglet.clock.schedule(obnov_stav) # zaregistruje danou funkci na tik hodin   
pyglet.app.run() # vše je nastaveno, ať začně hra!