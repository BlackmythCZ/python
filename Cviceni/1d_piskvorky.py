from random import randrange
from zamen import zamen
kolo = 0
pole = 'xxoxox-'
# pozice = int()

def vyhodnot(pole):
    if 'xxx' in pole:
        return 'x'
    elif 'ooo' in pole:
        return 'o'
    elif '-' not in pole:
        return '!'
    else:
        return '-'

def tah(pole, cislo_policka, symbol):
    pole = zamen(pole, cislo_policka, symbol)


def tah_hrace(pole):
    '''"Vrátí herní pole s daným symbolem umístěným na danou pozici"'''
    while True:
        pozice = int(input('Na jakou pozici chceš hrát? '))
        if pozice < 0 or pozice > 19:
            print('Zadej číslo mezi 0 a 19!')
        else:
            tah(pole, pozice, 'x')
            break


def tah_pocitace(pole):
    '''"Vrátí herní pole se zaznamenaným tahem počítače"'''
    while True:
        pozice = randrange(0, 19)

print(pole)
tah_hrace(pole)
print(pole)
tah_pocitace







    
