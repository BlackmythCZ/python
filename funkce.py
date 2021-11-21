#Definice funkce


#Ve slově 'slovo' zamění znak na pozici 'pozice' za 'novy_znak';
#výsledek bude v proměnné 'nove_slovo'.
'''
zacatek = slovo[:pozice]
konec = slovo[pozice + 1:]
nove_slovo = zacatek + novy_znak + konec
'''

def zamen(slovo, pozice, novy_znak):
    '''V daném slově zamění znak na dané pozici za daný nový znak'''
    zacatek = slovo[:pozice]
    konec = slovo[pozice + 1:]
    nove_slovo = zacatek + novy_znak + konec
    return nove_slovo

'''
print(zamen('kočka', 1, 'a'))
print(zamen('kačka', 2, 'p'))
'''

def napis_hlasku(nazev, skore):
    '''Popíše skóre. Název má být přivlastňovací přídavné jméno.'''
    print(nazev, 'skóre je', skore)
    if skore > 1000:
        print('Světový rekord!')
    elif skore > 100:
        print('Skvělé!')
    elif skore > 10:
        print('Ucházející.')
    elif skore > 1:
        print('Aspoň něco')
      
    else:
        print('Snad příště.')

'''
napis_hlasku('Tvoje', 256)
napis_hlasku('Protivníkovo', 5)
'''

def obsah_obdelniku(a, b):
    '''Funkce spočítá obsah obdélníku z hodnoty strany 'a' a strany 'b' '''
    obsah_obdelniku = a * b
    return obsah_obdelniku

'''
print('Obsah obdélniku je:', obsah_obdelniku(4, 5), 'cm2.')
'''

def ano_nebo_ne(otazka):
    '''Vrátí TGrue nebo False podle odpovědi uživatele'''
    while True:
        odpoved = input(otazka)
        if odpoved == 'ano':
            return True
        elif odpoved == 'ne':
            return False
        
        print('Nerozumím! Odpověz "ano" nebo "ne".')

'''
if ano_nebo_ne('Chceš si zahrát hru? ') == True:
    print('OK, ale nejdřív si ji musíš naprogramovat :)')
else:
    print('Tak si běž hrát ven.')
'''

from math import pi

def obsah_elipsy(a, b):
    '''Vrátí hodnotu obsahu elipsy s poloosami daných délek'''
    return pi * a * b

'''
print('Obsah elipsy s poloosami 3 a 5 je', obsah_elipsy(3, 5), 'cm2.')
'''

'''
# print a input jsou "venku" mimo definici funkce
x = float(input('Zadejte délku poloosy 1: '))
y = float(input('Zadejte délku poloosy 2: '))
print('Obsah elipsy od délce jedné poloosy', x, 'cm a druhé poloosy', y, 'cm je: ', obsah_elipsy(x, y))
'''

from math import pi
obsah = 0
a = 30

def obsah_elipsy(a, b):
    obsah = pi * a * b  # Přiřazení do `obsah`
    a = a + 3  # Přiřazení do `a`
    return obsah

print(obsah_elipsy(a, 20))
print(obsah)
print(a)
