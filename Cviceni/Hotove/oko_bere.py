from random import randrange

bodu_celkem = 0

while bodu_celkem < 21:
    print('Máš ', bodu_celkem, ' bodů.')
    odpoved = input('Chceš otočit kartu?')
    if odpoved == 'Ano' or odpoved == 'ano':
        karta = randrange(2, 11)
        print('Tvoje další karta má hodnotu ' + str(karta) + ' bodů')
        bodu_celkem += karta
    elif odpoved == 'Ne' or odpoved == 'ne':
        break
    else:
        print('Nerozumím. Odpovídej prosím "ano" nebo "ne".')

if bodu_celkem == 21:
    print('Gratuluji! Vyhrál jsi.')
elif bodu_celkem > 21:
    print('Bohužel jsi prohrál...')
else:
    print('Chybělo ti ', bodu_celkem, 'bodů. Hra skončila.')
