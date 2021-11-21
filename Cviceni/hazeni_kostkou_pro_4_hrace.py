# První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka. Potom hází další hráč,
# dokud nepadne šestka i jemu. Potom hází hráč třetí a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky
# potřeboval nejvíc hodů. (V případě shody vyhraje ten, kdo házel dřív.)
#Program by měl vypisovat všechny hody a nakonec napsat, kdo vyhrál.

from random import randrange

pocet_hodu_prvni_hrac = 1
pocet_hodu_druhy_hrac = 1
pocet_hodu_treti_hrac = 1
pocet_hodu_ctvrty_hrac = 1
prvni_hrac_hodil_6 = False
druhy_hrac_hodil_6 = False
treti_hrac_hodil_6 = False
ctvrty_hrac_hodil_6 = False

while True:
    prvni_hrac = randrange (1, 7)
    if prvni_hrac < 6:
        pocet_hodu_prvni_hrac += 1
        print(f'První hráč hodil {prvni_hrac}')
    else:
        print(f'První hráč hodil 6 po {pocet_hodu_prvni_hrac} hodech.')
        prvni_hrac_hodil_6 = True
        break

while True:
    druhy_hrac = randrange (1, 7)
    if druhy_hrac < 6:
        pocet_hodu_druhy_hrac += 1
        print(f'Druhý hráč hodil {druhy_hrac}')
    else:
        print(f'Druhý hráč hodil 6 po {pocet_hodu_druhy_hrac} hodech.')
        druhy_hrac_hodil_6 = True
        break

while True:
    treti_hrac = randrange (1, 7)
    if treti_hrac < 6:
        pocet_hodu_treti_hrac += 1
        print(f'Třetí hráč hodil {treti_hrac}')
    else:
        print(f'Třetí hráč hodil 6 po {pocet_hodu_treti_hrac} hodech.')
        treti_hrac_hodil_6 = True
        break

while True:
    ctvrty_hrac = randrange (1, 7)
    if ctvrty_hrac < 6:
        pocet_hodu_ctvrty_hrac += 1
        print(f'Čtvrtý hráč hodil {ctvrty_hrac}')
    else:
        print(f'Čtvrtý hráč hodil 6 po {pocet_hodu_ctvrty_hrac} hodech.')
        ctvrty_hrac_hodil_6 = True
        break

if (prvni_hrac_hodil_6 == False) or (druhy_hrac_hodil_6 == False) or (treti_hrac_hodil_6 == False) or (ctvrty_hrac_hodil_6 == False):
    print(f'Nekterý z hráčů 6 zatím nehodil.')
else:
    print(f'První hráč hodil 6 po {pocet_hodu_prvni_hrac} hodech. Druhý hráč hodil 6 po {pocet_hodu_druhy_hrac} hodech. Třetí hráč hodil 6 po {pocet_hodu_treti_hrac} hodech. Čtvrtý hráč hodil 6 po {pocet_hodu_ctvrty_hrac} hodech.')
    if (pocet_hodu_prvni_hrac > pocet_hodu_druhy_hrac) and (pocet_hodu_prvni_hrac > pocet_hodu_treti_hrac) and (pocet_hodu_prvni_hrac > pocet_hodu_ctvrty_hrac):
        print(f'Vyhrál první hráč, který hodil 6 po {pocet_hodu_prvni_hrac} hodech.')
    elif (pocet_hodu_druhy_hrac > pocet_hodu_prvni_hrac) and (pocet_hodu_druhy_hrac > pocet_hodu_treti_hrac) and (pocet_hodu_druhy_hrac > pocet_hodu_ctvrty_hrac):
        print(f'Vyhrál druhý hráč, který hodil 6 po {pocet_hodu_druhy_hrac} hodech.')
    elif (pocet_hodu_treti_hrac > pocet_hodu_prvni_hrac) and (pocet_hodu_treti_hrac > pocet_hodu_druhy_hrac) and (pocet_hodu_treti_hrac > pocet_hodu_ctvrty_hrac):
        print(f'Vyhrál třetí hráč, který hodil 6 po {pocet_hodu_treti_hrac} hodech.')
    else:
        print(f'Vyhrál čtvrtý hráč, který hodil 6 po {pocet_hodu_ctvrty_hrac} hodech.')