cisla = [1, 1, 2, 3, 5, 8, 13]
print(cisla)

for cislo in cisla:
    print(cislo)

seznam = [1, 'abc', True, None, range(10), len]
print(seznam)

print(cisla[2])

print(cisla[2:-3])

# Důležitá vlastnost seznamů, kterou nemají ani čísla, ani řetězce (a True/False/None už vůbec ne), je, že seznamy se dají měnit.
prvocisla = [2, 3, 5, 7, 11, 13, 17]
print(prvocisla)
prvocisla.append(19)
print(prvocisla)

a = [1, 2, 3] # vytvoření seznamu
b = a # tady se nový seznam nevytváří

# seznam vytvořený v prvním řádku má teď dvě jména: "a" a "b",
# ale stále pracujeme jenom s jedním seznamem

print(b)
a.append(4)
print(b)
print(a)

# Kromě metody append, která přidává jediný prvek, existuje metoda extend, která umí přidávat prvků víc. Prvky k přidání jí předáme ve formě seznamu:
dalsi_prvocisla = [23, 29, 31]
prvocisla.extend(dalsi_prvocisla)
print(prvocisla)

# Metoda extend umí pracovat i s jinými typy než se seznamy – ráda zpracuje cokoli, přes co umí cyklit for: např. jednotlivé znaky řetězců, řádky souborů, nebo čísla z range().
seznam = []
seznam.extend('abcdef')
seznam.extend(range(10))
print(seznam)

# Seznamům se dají i měnit jednotlivé prvky a to jednoduše tak, že do prvku přiřadíme, jako by to byla proměnná:
cisla = [1, 0, 3, 4]
cisla[1] = 2
print(cisla)

# řiřazovat se dá i do podseznamu – v tomto případě se podseznam nahradí jednotlivými prvky z toho, co přiřazujeme. Jako u extend můžeš do podseznamu opět přiřadit cokoli, co umí zpracovat for – seznam, řetězec, range() apod.
cisla = [1, 2, 3, 4]
cisla[1:-1] = [6, 5]
print(cisla)

# Přiřazením do podseznamu se dá i změnit délka seznamu, nebo některé prvky úplně odstranit:
cisla = [1, 2, 3, 4]
cisla[1:-1] = [0, 0, 0, 0, 0]
print(cisla)
cisla[1:-1] = []
print(cisla)

# Tenhle výše uvedený zápis pro mazání prvků je ale docela nepřehledný, a proto na to máme zvláštní příkaz jménem del:
cisla = [1, 2, 3, 4, 5, 6]
del cisla[-1]
print(cisla)
del cisla[3:5]
print(cisla)
del cisla # Maže i proměnné!
#print(cisla)

# Další mazací metody jsou:
# pop, která odstraní a vrátí poslední prvek v seznamu – například pokud mám seznam karet v balíčku, jde takhle jednoduše „líznout” kartu,
# remove, která najde v seznamu daný prvek a odstraní ho,
# clear, která vyprázdní celý seznam.

cisla = [1, 2, 3, 'abc', 4, 5, 6, 12]
posledni = cisla.pop()
print(posledni)
print(cisla)

cisla.remove('abc')
print(cisla)

cisla.clear()
print(cisla)