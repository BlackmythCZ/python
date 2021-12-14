# Tady je slovník, který má tři klíče, a k nim příslušné tři hodnoty:
ja = {'jméno': 'Anna', 'město': 'Brno', 'čísla': [3, 7]}

# Hodnoty ze slovníku můžeš získat podobně jako ze seznamu, jen místo indexu (pozice) použiješ klíč:
print(ja['jméno'])

# Zeptáš-li se na neexistující klíč, nebude se to Pythonu líbit:
# print(ja['věk'])

# Hodnoty jdou podle klíče i měnit:
ja['jazyk'] = 'Python'
print(ja)

# nebo přidávat:
del ja['čísla']
print(ja)

# Vyhledávací tabulka (lookup table), v ní mají typicky všechny hodnoty stejný typ:

cisla = {
    'Maruška': '153 85283',
    'Terka': '237 26505',
    'Renata': '385 11223',
    'Michal': '491 88047',
}

barva = {
    'hruška': 'zelená',
    'jablko': 'červená',
    'meloun': 'zelená',
    'švestka': 'modrá',
    'ředkvička': 'červená',
    'zelí': 'zelená',
    'mrkev': 'červená',
}

# Když dáš slovník do cyklu for, dostaneš klíče:
popisy_funkcí = {'len': 'délka', 'str': 'řetězec', 'dict': 'slovník'}
for klic in popisy_funkcí:
    print (klic)
# Existuje i metoda keys(), která vrací klíče.

# Pokud chceš hodnoty, stačí použít metodu values:
for hodnota in popisy_funkcí.values():
    print (hodnota)

# Většinou ale potřebuješ jak klíče tak hodnoty. K tomu mají slovníky metodu items, která bude v cyklu for dávat dvojice:
for klic, hodnota in popisy_funkcí.items():
    print('{}: {}'.format(klic, hodnota))

# V průběhu takového for cyklu nesmíš do slovníku přidávat záznamy, ani záznamy odebírat:
# for klic in popisy_funkcí:
#     del popisy_funkcí[klic]

# Slovník se dá vytvořit také pomocí funkce dict.
# Slovník je ovšem dost specifická struktura – čísla nebo typické seznamy na něj převádět nejdou.
# Můžeme ale na slovník převést jiný slovník. Nový slovník žije svým vlastním životem; následné změny se promítnou jen do něj.
barvy_po_tydnu = dict(barva)
for klic in barvy_po_tydnu:
    barvy_po_tydnu[klic] = 'černo-hnědo-' + barvy_po_tydnu[klic]
print(barva['jablko'])
print(barvy_po_tydnu['jablko'])

print(barva)
print(barvy_po_tydnu)

# Druhá věc, která jde převést na slovník, je sekvence dvojic klíč/hodnota:
data = [(1, 'jedna'), (2, 'dva'), (3, 'tři')]
nazvy_cisel = dict(data)

# funkce dict ještě brát pojmenované argumenty. Každé jméno argumentu převede na řetězec, použije ho jako klíč, a přiřadí danou hodnotu:
popisy_funkcí = dict(len = 'délka', str = 'řetězec', dict = 'slovník')
print(popisy_funkcí['len'])