zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

def vyber_chybne(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        if jmeno[0].islower() or prijmeni[0].islower():
            vysledek.append(zaznam)
    return vysledek

print(vyber_chybne(zaznamy))

def vyber_spravne(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        if not jmeno[0].islower() and not prijmeni[0].islower():
            vysledek.append(zaznam)
    return vysledek

print(vyber_spravne(zaznamy))

def oprav_chybne(seznam):
    vysledek = [] # vytvoří prázný seznam
    for zaznam in seznam: # provede cyklus pro každý řetězec ze seznamu
        jmeno_a_prijmeni = zaznam.split(' ') # naplní proměnnou seznamem, který obsahuje záznamy z řetězce oddělené mezerou
        jmeno = jmeno_a_prijmeni[0] # naplní proměnou prvním záznamem ze seznamu jmeno_a_prijmeni
        prijmeni = jmeno_a_prijmeni[1] # naplní proměnou druhým záznamem ze seznamu jmeno_a_prijmeni
        vysledek.append(jmeno.capitalize() + ' ' + prijmeni.capitalize()) # přidá do seznamu "vysledek" hodnoty jmen a příjmení s aplikovanou funkcí "capitalize", která nastaví první písmeno slova na velké
    return vysledek

print(oprav_chybne(zaznamy))
